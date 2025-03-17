from Models.Base import *
from Models.Users import Users
from Models.Statuses import Statuses
from Models.Payments import Payments

class Orders(Base):
    id = PrimaryKeyField()
    date = DateTimeField()
    payment_id = ForeignKeyField(Payments)
    delivery_data = CharField()
    client_id = ForeignKeyField(Users)
    status_id = ForeignKeyField(Statuses)


    class Meta:
        table_name = 'Orders'

if __name__ == '__main__':
    pass