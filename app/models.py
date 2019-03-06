from app import db, login
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), unique=True)

    def update_username(self, new_name, provider='orcid'):
        # Make sure the username is globally unique by adding a prefix based on
        # account provider
        if provider == 'orcid':
            self._username = "orcid_" + new_name
        else:
            # User's account was creating on the CONP portal itself
            self._username = "local_" + new_name

    @property
    def username(self):
        # Removes the prefix when a username just needs to be displayed and
        # we dont care about global uniqueness
        try:
            uname = self._username.split("_")[1]
        except AttributeError:
            uname = ""
        return uname

    def __repr__(self):
        return '<User {}>'.format(self.username)
