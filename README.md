# Django Blog Project

A full-featured blog application built with Django, containerized with Docker, and served through Nginx + Gunicorn in production.

## Features

- User authentication (registration, login, logout)
- Create, read, update, and delete blog posts
- Category and tag system for organizing posts
- Admin panel for content management
- Health check endpoint for monitoring
- Static and media file serving via Nginx
- PostgreSQL database backend
- Production-ready Docker setup with multi-stage builds

## Technologies Used

| Layer | Technology |
|---|---|
| Backend | Django 4.x, Python 3.13 |
| Database | PostgreSQL 15 |
| Web Server | Nginx (reverse proxy) |
| App Server | Gunicorn (WSGI) |
| Containerization | Docker, Docker Compose |
| Version Control | Git, GitHub |

## Project Structure

```
dscc_cw/
├── blog/                   # Main blog application
├── config/                 # Django project configuration
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── nginx/
│   ├── Dockerfile
│   └── nginx.conf
├── .dockerignore
├── .env.example            # Environment variables template
├── .gitignore
├── docker-compose.yml      # Production compose file
├── docker-compose.dev.yml  # Development compose file
├── Dockerfile              # Multi-stage production Dockerfile
├── gunicorn.conf.py        # Gunicorn configuration
├── manage.py
└── requirements.txt
```

## Local Setup Instructions

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed
- [Docker Compose](https://docs.docker.com/compose/install/) installed
- Git installed

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```

2. **Create your environment file**
   ```bash
   cp .env.example .env
   ```
   Then edit `.env` and fill in your values (see Environment Variables section below).

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

## Deployment Instructions

### Server Requirements

- Ubuntu 24.04 LTS
- Docker and Docker Compose installed
- Ports 80 and 443 open (UFW configured)

### Steps

1. **SSH into your server**
   ```bash
   ssh azureuser@YOUR_SERVER_IP
   ```

2. **Install Docker**
   ```bash
   curl -fsSL https://get.docker.com | sh
   sudo usermod -aG docker $USER
   ```

3. **Clone the repository on the server**
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   nano .env  # fill in production values
   ```

5. **Start the application**
   ```bash
   docker compose up -d --build
   ```

6. **Run migrations**
   ```bash
   docker compose exec web python manage.py migrate
   ```

7. **Create a superuser**
   ```bash
   docker compose exec web python manage.py createsuperuser
   ```

The application will be accessible at `http://YOUR_SERVER_IP`.

## Environment Variables

Create a `.env` file based on `.env.example`:

| Variable | Description | Example |
|---|---|---|
| `DJANGO_SECRET_KEY` | Django secret key (keep this secret!) | `your-secret-key-here` |
| `DJANGO_SETTINGS_MODULE` | Settings module to use | `config.settings.development` |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts | `localhost,127.0.0.1` |
| `POSTGRES_DB` | PostgreSQL database name | `blog_db` |
| `POSTGRES_USER` | PostgreSQL username | `bloguser` |
| `POSTGRES_PASSWORD` | PostgreSQL password | `yourpassword` |
| `POSTGRES_HOST` | PostgreSQL host (use `db` inside Docker) | `db` |
| `POSTGRES_PORT` | PostgreSQL port | `5432` |

> **Never commit your `.env` file to Git.** It is listed in `.gitignore` by default.

## Screenshots

> Add screenshots of your running application here.
> Example:
> ![Blog Post List](screenshots/post_list.png)
> ![Admin Panel](screenshots/admin.png)

## API Endpoints

| URL | Description |
|---|---|
| `/` | Blog post list |
| `/post/<id>/` | Blog post detail |
| `/post/new/` | Create new post (auth required) |
| `/post/<id>/edit/` | Edit post (author only) |
| `/post/<id>/delete/` | Delete post (author only) |
| `/category/<id>/` | Posts by category |
| `/health/` | Health check (returns JSON) |
| `/admin/` | Django admin panel |
