from peewee import PrimaryKeyField, CharField

from Models.Base import *
from app import connect


class Statuses(Base):
    id = PrimaryKeyField
    status_name = CharField()
    class Meta:
        table_name = 'Statuses'

if __name__ == "__main__":
 pass