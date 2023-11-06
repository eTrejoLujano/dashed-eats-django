# Dashed Eats
A food delivery web application built with Javascript and Python that gives users the power to conveniently order groceries and meals from any location via the Google Maps API.

[Frontend Repository](https://github.com/eTrejoLujano/dashed-eats-react)

## Project Overview
### Technologies Used
- React: Used as the primary frontend library.
- Redux Toolkit: For state management.
- Django: Used as the primary backend framework. 
- Tailwind CSS: Used to design the responsive user interface (UI).
- Amazon Web Services: Used for deployment of the backend infrastructure 

### Project's backend Structure 
The project's codebase is organized as follows:
- `fixtures`: Holds all of the seed data for the project.
- `manage.py`: The command-line utility for the Django project.
- `instadash/`: This directory contains the source code for the project
  - `__init__.py`: Holds several different requests used to interact with the Django API.
  - `admin.py`: Various components used in the project.
  - `asgi.py`: The slices for redux toolkit's state management.
  - `managers.py`: The main application component.
  - `models.py`: The entry point of the application.
  - `serializers.py`: The entry point of the application.
  - `settings.py`: The entry point of the application.
  - `urls.py`: The entry point of the application.
  - `views.py`: The entry point of the application.
  - `wsgi.py`: The entry point of the application.

## Getting Started
To run this project locally, follow these steps:
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment.
4. Activate your virtual environment, if not already activated.
5. Install the required dependies using `pip install -r requirements.txt`.
6. Obtain a [Google Map API Key](#Google-Maps-API-Key) and generate a [Django secret key](https://djecrety.ir/).
7. Create an `.env` file with `GOOGLE_KEY` set to the Google Map API Key and `SECRET_KEY` as the Django secret key.
8. Create a database in your PostgreSQL environment on your machine.
9. Go to the settings.py file in the `instadash/` directory.
10. Comment out lines 178-202 and comment in lines 166-176.
11. Fill out your database information on lines 166-176.
12. Start the development server with `python3 manage.py runserver`.

This will launch the application locally for testing and development.

## Database Schema

![Screenshot 2023-11-05 at 11 30 20 PM](https://github.com/eTrejoLujano/dashed-eats-django/assets/85711028/b2b56a8b-df9c-4ab7-9848-aeb9a328ae48)

## Google Maps API Key
To obtain a Google Maps API Key for this project, follow these steps:
  1. Go to the [Google Developer Console](https://console.developers.google.com).
  2. Create a new project.
  3. Manage API's and enable the following required Google Maps Platform APIs for this project:
     - Maps JavaScript API
     - Address Validation API
     - Geocoding API
     - Places API
     - Distance Matrix API
  4. Create credentials to obtain the Maps API key.
