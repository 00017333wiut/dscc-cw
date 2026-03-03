# Stage 1: Builder
FROM python:3.13-alpine AS builder

WORKDIR /app

RUN apk add --no-cache \
    gcc musl-dev postgresql-dev


RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Production
FROM python:3.13-slim AS production

# Create user FIRST before anything else
RUN groupadd --gid 1000 appgroup && \
    useradd --uid 1000 --gid appgroup --shell /bin/bash --create-home appuser

WORKDIR /app

RUN apk add --no-cache \
    postgresql-libs netcat-openbsd

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY --chown=appuser:appgroup . .

RUN mkdir -p staticfiles media && \
    chown -R appuser:appgroup staticfiles media && \
    touch gunicorn.ctl && \
    chown appuser:appgroup gunicorn.ctl

USER appuser

EXPOSE 8000