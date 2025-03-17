from Models.Base import *
from Models.Goods import Goods
from Models.Order import Orders

class Good_Orders(Base):
    id=PrimaryKeyField()
    good_id = ForeignKeyField(Goods)
    order_id = ForeignKeyField(Orders)

    class Meta:
        table_name = 'Good_Orders'

if __name__ == '__main__':
    pass