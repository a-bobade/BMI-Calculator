# BMI-Calculator
This is a BMI-calculator application built with Django 3 and Django REST Framework.
# Project Summary
- The application calculates the BMI(Body Mass Index) of users. Enter your Weight (in kg) and Height (in cm), then click on Calculate to get your BMI.

You can save your BMI for future reference, you can only save data when you are logged in. Creating an account is easy, by clicking on Sign Up.

The BMI is categorized in 4 parts; Underweight, Healthy weight, Overweight and Obese.

The project can be viewed in web interface and also through API. You can view the API by using the URL http://127.0.0.1:8000/api 

SQLite was used for the database.
# Running this project
- To get this project up and running you should start by having Python installed on your computer. 

- Activate the virtual environment with:\
  venv\Scripts\activate

- Clone or download this repository and open it in your editor of choice. 

- Then install the project dependencies with:\
  pip install -r requirements.txt

- Make migrations with these commands:\
  python manage.py makemigrations\
  python manage.py migrate

- Now you can run the project with this command:\
  python manage.py runserver
