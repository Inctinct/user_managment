# user_managment
To start the application you need:

git clone https://github.com/Inctinct/user_managment/
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

To start with docker:

git clone https://github.com/Inctinct/user_managment/
docker-compose build
docker-compose up -d
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser


If we want to run the application locally, we use the option without docker.
If there is a need to start as a separate container, we use the docker option.
For deployment, you need to change the settings.py
namely, specify the host on which it will be deployed, set up the CORS to be able to send requests to the api.
I used sqlite3 because I did not see the need to connect another database, 
for good it is necessary to connect posgtres(or another), then you need to change the DATABASE settings,depending on the selected database.
All important data (passwords, addresses, etc.) should be stored in a .env file
