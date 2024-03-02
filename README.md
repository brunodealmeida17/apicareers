# API Documentation

  

## Routes

  

-  **GET /careers/**

- Description: Retrieve a list of all careers.

- Response: List of career objects.

  

-  **GET /careers/{OBJECT_ID}/**

- Description: Retrieve details of a specific career.

- Response: Career object.

  

-  **POST /careers/**

- Description: Create a new career.

- Request Body: Career object.

- Response: Created career object.

  

-  **PUT /careers/{OBJECT_ID}/**

- Description: Update an existing career.

- Request Body: Updated career object.

- Response: Updated career object.

  

-  **DELETE /careers/{OBJECT_ID}/**

- Description: Delete an existing career.

- Response: Success message.

  

## Models

  

### Career

-  **id** (int): The unique identifier for the career.

-  **username** (str): The username of the career owner.

-  **create_datetime** (datetime): The datetime when the career was created.

-  **title** (str): The title of the career.

-  **content** (str): The content of the career.

  

Using the API Locally

Requirements

Python 3.6 or higher

  

Django 2.2.9

django-filter 2.2.0

djangorestframework 3.11.0

Markdown 3.1.1 - pytz 2019.3

sqlparse 0.3.0

  

## Using the API Locally

  

### Requirements

- Python 3.10 or higher

- Django 5.0.2-

- djangorestframework 3.14.0

  

### Installation

1. Make sure you have Python installed on your system. You can download the latest version of Python at [python.org](https://www.python.org/).

  

2. Clone this repository to your local development environment:

	`git clone https://github.com/brunodealmeida17/apicodeleap`

  

3. Create a virtual environment to isolate the API dependencies. Navigate to the project root directory and execute the following command:

	`python -m venv myenv`

This will create a virtual environment named "myenv".

  

4. Activate the virtual environment:

- On Windows:

	```myenv\Scripts\activate```

- On macOS/Linux:

	```	source myenv/bin/activate```

  

5. Install the API dependencies. In the project root directory, execute the following command:

	`pip install -r requirements.txt`

  

This will install all the necessary dependencies to run the API locally.

  

6. Apply the database migrations:

	`python manage.py migrate`

  

7. Start the Django development server:

	`python manage.py runserver`

  
  

# Deploy Server Linux/Ubuntu

  

## Introduction

This script automates the setup process for a Django project with Celery, Redis, Django Channels, and Gunicorn on a Linux server.

  

## Usage

1.  **Download the script**:

- Clone the repository containing the deployment script:

  

	```git clone https://github.com/brunodealmeida17/apicodeleap```

  

2.  **Navigate to the directory**:

- Move into the cloned directory:

	```cd apicodeleap```

  

3.  **Run the script**:

- Execute the deployment script:

	```sudo bash install.sh```

  

4.  **Follow the prompts**:

- The script will prompt you to enter the SERVER_NAME and PORTA (port) for your server.

  

5.  **Installation process**:

- The script will automatically install the required dependencies, create necessary directories, configure NGINX, set up Gunicorn, generate SSL/TLS certificates (if desired), and start the server.

  

6.  **Check status**:

- After running the script, check the status of Gunicorn and NGINX services:

	```sudo systemctl status your_app_name.service```
	```sudo systemctl status nginx```

  

7.  **Access the application**:

- Once the deployment process is complete, you can access your Django application using the configured SERVER_NAME and PORTA (port).