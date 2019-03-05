# CONP Authentication 

This is the authentication application used by `conp-portal` 
login and authenticate users

### Requirements

This code requires Python 3.7 and PostgreSQL 9.5

### Python Virtual Environment

Create a Python virtual environment called `venv` and install Flask dependencies

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    
### Database set up
After installing PostgreSQL you'll need to create an empty database. Run
`createdb conp-auth` to do this. By default the app will search for a database
named 'conp-auth' on localhost, but to override this you can create an
environment variable named 'DATABASE_URL' that points to yours.

Example:
```shell
export DATABASE_URL="postgresql://[db_name:db_pass@]<hostname>/<database_name>"
```

### Run Application

You can run the application locally with 

    flask run
    
The application will be live on `http://127.0.0.1:5000/`
    

### Deployment
    
This flask application is deployed on Heroku. More information will be available soon