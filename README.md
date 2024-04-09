# Pizza-Resturant

Welcome to the Pizza Restaurant API! This API provides endpoints to manage pizza restaurants and their associated pizzas. You can perform operations like fetching restaurants, adding new pizzas, and deleting restaurants.

Getting Started
To run this API locally, follow these steps:

**Prerequisites**
Python 3.x installed on your machine
Pip (Python package installer)
Virtualenv 
Installation
Clone this repository to your local machine:
Navigate to the project directory:

cd pizza-restaurant-api
Create and activate a virtual environment 
navigate to server directory
Install the required dependencies:
run pip freeze > requirement.txt

pip install -r requirements.txt
Running the API
Set the Flask app and run the development server:

export FLASK_APP=app.py
export FLASK_ENV=development
flask run
The API should now be running locally at http://127.0.0.1:5555/.

**API Endpoints**
GET /restaurants: Retrieve a list of all restaurants.
GET /restaurants/<id>: Retrieve details of a specific restaurant by ID.
DELETE /restaurants/<id>: Delete a restaurant by ID.
GET /pizzas: Retrieve a list of all available pizzas.
POST /restaurant_pizzas: Add a new pizza to a specific restaurant.