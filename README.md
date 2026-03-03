# Django Blog Project

A full-featured blog application built with Django, containerized with Docker, and served through Nginx + Gunicorn in production. Deployed on Oracle Cloud with SSL via Let's Encrypt and automated CI/CD via GitHub Actions.

🌐 **Live at:** https://dscc-cw-blog.duckdns.org

---

## Features

- User authentication (login, logout)
- Create, read, update, and delete blog posts
- Category and tag system with pre-populated options
- Author-only edit and delete permissions
- Admin panel for content management
- Health check endpoint for monitoring
- Static and media file serving via Nginx
- PostgreSQL database backend
- Production-ready Docker setup with multi-stage builds
- Automated CI/CD pipeline via GitHub Actions

---

## Technologies Used

| Layer | Technology |
|---|---|
| Backend | Django 6.0.2, Python 3.13 |
| Database | PostgreSQL 15 |
| Web Server | Nginx (reverse proxy + SSL termination) |
| App Server | Gunicorn (WSGI) |
| Containerization | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| Cloud | Oracle Cloud (Ubuntu 24.04) |
| SSL | Let's Encrypt (Certbot) |
| Version Control | Git, GitHub |

---

## Project Structure

```
dscc_cw/
├── .github/
│   └── workflows/
│       └── deploy.yml          # CI/CD pipeline
├── blog/                       # Main blog application
│   ├── migrations/
│   ├── templates/blog/
│   │   ├── post_list.html
│   │   ├── post_detail.html
│   │   ├── post_form.html
│   │   ├── post_confirm_delete.html
│   │   └── category_posts.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
├── config/                     # Django project configuration
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf              # Nginx config with HTTPS
├── .dockerignore
├── .env.production.example
├── .gitignore
├── .gitattributes
├── docker-compose.yml          # Production compose file
├── docker-compose.dev.yml      # Development compose file
├── Dockerfile                  # Multi-stage production Dockerfile
├── gunicorn.conf.py            # Gunicorn configuration
├── pytest.ini                  # Test configuration
├── manage.py
└── requirements.txt
```

---

## Local Setup Instructions

### Prerequisites

- [Docker Desktop](https://docs.docker.com/get-docker/) installed and running
- Git installed

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/00017333wiut/dscc-cw.git
   cd dscc-cw
   ```

2. **Create your environment file**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and fill in your values (see Environment Variables below).

3. **Build and start the containers**
   ```bash
   docker compose up --build
   ```

4. **Access the application**
   - App: http://localhost:8080
   - Admin: http://localhost:8080/admin
   - Health check: http://localhost:8080/health/

5. **Create a superuser** (in a new terminal)
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

---

## Deployment Instructions

### Server Requirements

- Ubuntu 24.04 LTS (Oracle Cloud Free Tier)
- Docker and Docker Compose installed
- UFW firewall configured (ports 22, 80, 443)
- Domain pointing to server IP
- SSL certificate from Let's Encrypt

### Manual Deployment Steps

1. **SSH into your server**
   ```bash
   ssh -i ~/.ssh/oracle.key ubuntu@YOUR_SERVER_IP
   ```

2. **Install Docker**
   ```bash
   curl -fsSL https://get.docker.com | sh
   sudo usermod -aG docker $USER
   newgrp docker
   ```

3. **Configure firewall**
   ```bash
   sudo ufw allow 22/tcp
   sudo ufw allow 80/tcp
   sudo ufw allow 443/tcp
   sudo ufw enable
   sudo iptables -I INPUT 6 -m state --state NEW -p tcp --dport 80 -j ACCEPT
   sudo iptables -I INPUT 6 -m state --state NEW -p tcp --dport 443 -j ACCEPT
   sudo netfilter-persistent save
   ```

4. **Clone the repository**
   ```bash
   git clone https://github.com/00017333wiut/dscc-cw.git
   cd dscc-cw
   ```

5. **Create production environment file**
   ```bash
   nano .env
   ```

6. **Obtain SSL certificate**
   ```bash
   sudo certbot certonly --standalone -d your-domain \
     --email your@email.com --agree-tos --no-eff-email
   ```

7. **Start the application**
   ```bash
   docker compose up -d --build
   docker compose exec web python manage.py createsuperuser
   ```

### Automated Deployment (CI/CD)

Every push to `main` automatically:
1. Runs flake8 linting and pytest tests
2. Builds and pushes Docker image to Docker Hub (tagged `latest` and commit SHA)
3. SSHs into the server, pulls latest code, restarts containers, runs migrations and collectstatic

---

## Environment Variables

Create a `.env` file based on `.env.example`:

| Variable | Description | Example |
|---|---|---|
| `DJANGO_SECRET_KEY` | Django secret key | `your-secret-key-here` |
| `DJANGO_SETTINGS_MODULE` | Settings module | `config.settings.production` |
| `ALLOWED_HOSTS` | Comma-separated allowed hosts | `dscc-cw-blog.duckdns.org` |
| `POSTGRES_DB` | PostgreSQL database name | `blog_db` |
| `POSTGRES_USER` | PostgreSQL username | `bloguser` |
| `POSTGRES_PASSWORD` | PostgreSQL password | `yourpassword` |
| `POSTGRES_HOST` | PostgreSQL host | `db` |
| `POSTGRES_PORT` | PostgreSQL port | `5432` |

> **Never commit your `.env` file to Git.** It is listed in `.gitignore`.

### GitHub Actions Secrets Required

| Secret | Description |
|---|---|
| `DOCKER_USERNAME` | Docker Hub username |
| `DOCKER_PASSWORD` | Docker Hub password or access token |
| `VM_HOST` | Server public IP |
| `VM_USER` | SSH username (`ubuntu`) |
| `SSH_KEY` | Private SSH key contents |

---

## Pages & URLs

| URL | Description | Auth Required |
|---|---|---|
| `/` | Blog post list | No |
| `/post/<id>/` | Post detail | No |
| `/post/new/` | Create new post | Yes |
| `/post/<id>/edit/` | Edit post | Author only |
| `/post/<id>/delete/` | Delete post | Author only |
| `/category/<id>/` | Posts by category | No |
| `/accounts/login/` | Login page | No |
| `/accounts/logout/` | Logout | Yes |
| `/health/` | Health check (JSON) | No |
| `/admin/` | Django admin panel | Staff only |

---

## Running Tests

```bash
# Run all tests
python manage.py test

# With pytest
pytest
```

---
