from Models.Base import *
from flask_login import UserMixin

class Users(UserMixin,Base):
    id = PrimaryKeyField()
    login = CharField(unique=True)
    password = CharField()
    roles_id = ForeignKeyField
    class Meta:
        table_name = 'Users'

if __name__ == "__main__":
    pass