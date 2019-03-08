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
After installing PostgreSQL there are a few steps needed to get your database
set up.

1. Run `createdb conp-auth` to create an empty database named 'conp-auth'.
2. Tell the app how to find your database. If no settings are provided it
will try to connect to a database on localhost named 'conp-auth'. If you need
to override this you can set an environment variable named 'DATABASE_URL' to
point to the URL, as shown in the example below
```shell
export DATABASE_URL="postgresql://[db_name:db_pass@][hostname]/database_name"
```
3. Create the tables. This is done by running:
```
flask db upgrade
```

### ORCID set up
To manage accounts using ORCID you have to first register your app. Instructions
are here: https://support.orcid.org/hc/en-us/articles/360006897174 When setting
your 'Redirect URIs' use: `<your machine's hostname>:5000/callback/orcid`

After this you need to take the 'Client ID' and 'Client secret' from the
developer tools page and add them as two environment variables.

```shell
export OAUTH_ORCID_ID=<your-client-id>
export OAUTH_ORCID_SECRET=<your-client-secret>
```

**Note:** In order for ORCID to communicate with your development server the
server needs to listen on address 0.0.0.0 instead of 127.0.0.1. The easiest way
to do this is to run flask with:

```
./oauth_run.py
```

### Run Application

You can run the application locally with

    flask run

The application will be live on `http://127.0.0.1:5000/`


### Deployment

This flask application is deployed on Heroku. More information will be available soon
