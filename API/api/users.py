# flask packages
from flask_bcrypt import generate_password_hash, check_password_hash
from mongoengine import (Document,
                         EmbeddedDocument,
                         EmbeddedDocumentField,
                         StringField,
                         EmailField,
                         BooleanField)


class Access(EmbeddedDocument):
    """
    Custom EmbeddedDocument to set user authorizations.

    :param user: boolean value to signify if user is a user
    :param admin: boolean value to signify if user is an admin
    """
    user = BooleanField(default=True)
    admin = BooleanField(default=False)


class Users(Document):
    email = EmailField(required=True, unique=True)
    password = StringField(required=True, min_length=6, regex=None)
    access = EmbeddedDocumentField(Access, default=Access(user=True, admin=False))
    name = StringField(unique=False)

    def generate_pw_hash(self):
        self.password = generate_password_hash(password=self.password).decode('utf-8')

    def check_pw_hash(self, password: str) -> bool:
        return check_password_hash(pw_hash=self.password, password=password)

    def save(self, *args, **kwargs):
        # Overwrite Document save method to generate password hash prior to saving
        self.generate_pw_hash()
        super(Users, self).save(*args, **kwargs)
