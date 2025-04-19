# Local Mail Service

This is a simple local mail service built using Flask, SQLAlchemy, and Flask-Login. It supports user authentication, composing emails, and viewing an inbox.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up the database:
   ```bash
   python create_db.py
   ```

## Run

To start the application, run:

```bash
python run.py
```

The app will start in debug mode and be accessible at `http://127.0.0.1:5000/`.

## Configuration

The application configuration is located in `instance/config.py`. By default, it uses a local SQLite database (`mail.db`) and has a secret key set.

SMTP functionality is currently disabled in the configuration. If you want to enable email sending via SMTP, you will need to update the SMTP settings in `instance/config.py`.

## Features

- User authentication (login, registration, logout) using Flask-Login
- Compose and send emails locally within the app
- View inbox with received emails
- Database management with SQLAlchemy and Flask-Migrate

## Project Structure

- `app/` - Application package containing routes, models, forms, and templates
- `create_db.py` - Script to create database tables
- `run.py` - Entry point to run the Flask application
- `instance/config.py` - Configuration file (not included in version control)
- `requirements.txt` - Python dependencies

## Usage

- Register a new user account
- Log in with your credentials
- Compose and send emails to other users
- View your inbox to read received emails
