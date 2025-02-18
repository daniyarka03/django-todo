# Todo Application

A Django REST framework application for managing todo tasks with image processing capabilities and LeetCode problem solutions.

## Features

- CRUD operations for todo tasks
- Image processing (grayscale conversion and resizing) using OpenCV
- LeetCode problem solutions implemented as API endpoints
- Comprehensive test coverage
- Docker support

## Setup and Installation

1. Clone the repository  
2. Install dependencies: `pip install -r requirements.txt`  
3. Run migrations: `python manage.py migrate`  
4. Start the server: `python manage.py runserver`  
5. Create a `.env` file and add the following:  