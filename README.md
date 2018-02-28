
# A Dockerized  Django application, Postgres database

This Application scrapes data from https://coinmarketcap.com/ and stores the entries of all coins on the site. The update button will run the web Crawler and update or create new entires as needed.

Features of the Crawler:
* Uses multithreaded processing

## This is an example project using the following technologies:
* Docker with Docker Compose
* nginx, gunicorn
* React (under construction)
* Django Restful Api (under construction)

## Prerequesites
Must have docker installed:
https://www.docker.com/community-edition#/download

# Setup Local Environment

1. Create .env file
 
###### Here's a Sample
```
 SECRET_KEY='#_r+1boq=zxhknws&0-8l)fi77tp#%if+ii%$ek6h86_iv3q%&'
 DEBUG=true
 DJANGO_SETTINGS_MODULE=django_config.settings.local
 ALLOWED_HOSTS= 127.0.0.1 0.0.0.0
 DATABASE_URL=postgres://django:1234@postgres:5432/boilerplate
 DJANGO_ADMIN_URL=^admin/
 
 MAILGUN_API_KEY=[mailgun-api-key]
 MAILGUN_DEFAULT_FROM_EMAIL=[email]
 
 
 POSTGRES_PASSWORD=1234
 POSTGRES_USER=django
 POSTGRES_DB=boilerplate
 
 EMAIL_PORT=1025
 EMAIL_HOST=localhost
 EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
 DEFAULT_FROM_EMAIL=admin@gmail.com
```

1. npm install
2. make docker-build-dev
3. make docker-up-dev

#### Visit http://localhost:8000

* To access admin: User:admin, Password:admin. (may neeed to restart server for the first time)
* Click Scrape Button!
![alt text](screenshots/screenshot.png "description")

### ToDo:
1. Convert to Restful API
2. Transfer frontend to React
3. Production Environment still has issues
