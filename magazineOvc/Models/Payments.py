from unicodedata import decimal

from Models.Base import *

class Payments(Base):
    id = PrimaryKeyField()
    payment = DecimalField(max_digits=6, decimal_places=2)
    date = DateTimeField()
    class Meta:
        table_name = 'Payments'

if __name__ == '__main__':
    pass