import os
SECRET_KEY = os.environ.get('SECRET_KEY') or 'change_this_to_a_secure_random_key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///mail.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# SMTP Configuration
# Removed SMTP configuration as SMTP functionality is disabled
# SMTP_SERVER = os.environ.get('SMTP_SERVER') or 'smtp.example.com'
# SMTP_PORT = int(os.environ.get('SMTP_PORT') or 587)
# SMTP_USERNAME = os.environ.get('SMTP_USERNAME') or 'your_email@example.com'
# SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD') or 'your_email_password'
