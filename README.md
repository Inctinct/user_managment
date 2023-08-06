# user_managment
To start the application you need:
  1. git clone https://github.com/Inctinct/user_managment/
  2. pip install -r requirements.txt

    Set the environment and DATABASE variables according to your requirements.
    (allowed_hosts, secret_key, debug, database)
  3. python manage.py makemigrations
  4. python manage.py migrate
  5. python manage.py createsuperuser
  6. python manage.py runserver


User registration requires an email address and a password.
The user can also set the profile fields during registration (I chose the phone, first name, last name). 
The parameters for registration and profile can be changed in models.py.
The password is hashed into the database
After registration, the user can log in and receive tokens.
The user can get data on the profile, as well as change them.
Profile data can be customized in the models.py file.
The user can also delete his account.

  API deployed to Render.com - https://user-managment-unxs.onrender.com

  Endpoints:
  1. api/register - registration with email and password, optional phone, first_name, second_name (POST)
  3. api/login - email and phone. In response access and refresh tokens (POST)
  4. api/proile - GET for profile information, PUT for update profile information, DELETE for delete user account
              
   
