# Backend Project

A Flask-based backend application built with Python. This project is used to practice API development, database management, and application configuration.

## Setup

To set up the project:

1. Clone the repository from GitHub.
2. Open the project folder in your terminal.
3. Create a virtual environment with `python3 -m venv .venv`.
4. Activate it with `source .venv/bin/activate`.
5. Install the required packages with `pip install -r requirements.txt`. 

## Environment Variables

1. Copy `.env.example` to `.env`.
2. Update the values in `.env` for your local setup.
3. Set a secure `JWT_SECRET` for your application.

## Running the App

1. Make sure your virtual environment is activated.
2. Start the Flask application by running:

   ```bash
   flask --app "api_project:create_app()" run
   ```