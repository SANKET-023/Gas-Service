
# Gas Utility Service Request Application

A Django-based web application for managing gas utility service requests, designed for scalability to handle high volumes of customer service requests. The app allows customers to register, submit service requests, track their request status, and view their account information. Customer support representatives can also manage requests from the admin interface.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Variables](#environment-variables)
- [Running the Project](#running-the-project)
- [Usage](#usage)
- [Folder Structure](#folder-structure)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

The **Gas Utility Service Request Application** helps a gas utility company manage customer service requests efficiently, reducing wait times and improving service quality. This application is structured to support high volumes of users, scalable for a country-level user base. It has two primary user types: **customers** and **customer support representatives**.

---

## Features

### Customer Features
- **Account Registration**: Allows new customers to register and create an account.
- **Service Request Submission**: Customers can submit requests, specify request types, provide details, and upload relevant files.
- **Request Tracking**: Customers can view the status of their requests and see when they were submitted and resolved.
- **Account Information**: Access to account details and service history.

### Customer Support Representative Features
- **Request Management**: Customer support representatives can view, update, and resolve customer service requests from the Django admin panel.
- **User Management**: Admin users can manage customer data, including resetting passwords and updating account details.

---

## Requirements

- **Python 3.8+**
- **Django 4.x**
- **PostgreSQL** or **SQLite** (for development)
- **Other dependencies**: Listed in `requirements.txt`

---

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/gas-utility-service-app.git
cd gas-utility-service-app
```

### Step 2: Set Up Virtual Environment

Create and activate a virtual environment:

```bash
# On macOS and Linux
python3 -m venv env
source env/bin/activate

# On Windows
python -m venv env
env\Scripts\activate
```

### Step 3: Install Dependencies

Install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

This project uses a `.env` file to manage sensitive information. Create a `.env` file in the root directory and add the following variables:

```plaintext
# .env

SECRET_KEY='your-secret-key'
DEBUG=True

# Database configuration (PostgreSQL example)
DB_NAME='your_database_name'
DB_USER='your_database_user'
DB_PASSWORD='your_database_password'
DB_HOST='localhost'
DB_PORT='5432'

# Email settings
EMAIL_HOST='smtp.example.com'
EMAIL_HOST_USER='your-email@example.com'
EMAIL_HOST_PASSWORD='your-email-password'
EMAIL_PORT=587
EMAIL_USE_TLS=True
```

### Notes:
- Make sure to set `DEBUG=False` in production for security purposes.
- Set up a secure and unique `SECRET_KEY` for each environment.

---

## Running the Project

### Step 1: Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 2: Create a Superuser

Create an admin user to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to set a username, email, and password for the admin.

### Step 3: Run the Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000` to access the application.

---

## Usage

### Customer Workflow
1. **Register**: Go to `/register/` to create a customer account.
2. **Submit a Service Request**: After logging in, go to `/requests/submit/` to submit a new service request.
3. **Track Request Status**: View the status and resolution time of each submitted request at `/requests/track/<request_id>/`.

### Admin Workflow (Customer Support)
1. **Log in to the Admin Panel**: Access the admin panel at `/admin/`.
2. **Manage Requests**: View and manage customer service requests from the admin panel.
3. **User Management**: Manage customer accounts and permissions through the Django admin interface.

---

## Folder Structure

```
gas-utility-service-app/
│
├── gas_service_app/             # Main project folder
│   ├── settings/                 # Contains base, local, and production settings
│   ├── urls.py                   # URL routing for the project
│   └── wsgi.py                   # WSGI entry point for production
│
├── service_requests/             # App handling service requests
│   ├── templates/                # HTML templates
│   ├── models.py                 # Database models
│   ├── views.py                  # Views for handling requests
│   ├── forms.py                  # Forms for user input
│   └── urls.py                   # URL routing specific to the app
│
├── .env                          # Environment variables file
├── .gitignore                    # Specifies files to ignore in version control
├── requirements.txt              # Project dependencies
└── manage.py                     # Django management script
```

---

## Testing

Django’s testing framework is used for unit and integration tests.

### Running Tests

```bash
python manage.py test
```

### Sample Tests

You can write tests for:
- **User Registration**
- **Service Request Submission**
- **Request Tracking**

For detailed information on testing Django applications, refer to the [Django Testing Documentation](https://docs.djangoproject.com/en/stable/topics/testing/).

---

## Deployment

To deploy this application in a production environment, follow these general steps:

1. **Set `DEBUG=False`** in your `.env` file or production settings.
2. **Configure Allowed Hosts** in `settings/production.py`.
3. **Set Up a Production Database** (e.g., PostgreSQL) and add credentials to `.env`.
4. **Configure a Web Server** (e.g., Nginx) and an application server (e.g., Gunicorn).
5. **Set Up Static and Media Files**:
   - Run `python manage.py collectstatic` to collect static files.
6. **Use a Process Manager** (e.g., Supervisor) to keep the app running.
7. **Use HTTPS** for secure communication.

For step-by-step deployment instructions, refer to [Django’s Deployment Guide](https://docs.djangoproject.com/en/stable/howto/deployment/).

---

## Contributing

Contributions are welcome! To contribute:

1. **Fork the repository**.
2. **Create a new branch** with a descriptive name:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit your changes** with descriptive messages:
   ```bash
   git commit -m "Add a new feature"
   ```
4. **Push to your fork** and create a pull request:
   ```bash
   git push origin feature/your-feature-name
   ```

For larger changes, please open an issue to discuss your idea first.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
---

### Acknowledgments

This application was built using [Django](https://www.djangoproject.com/) and follows best practices for a scalable web application.

--- 

This README file serves as a comprehensive guide for your project, ensuring it is well-documented for users, contributors, and collaborators. Let me know if you need any additions or modifications! 
