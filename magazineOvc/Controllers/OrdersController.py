from itertools import count

from Models.Order import *


class OrdersController:

    @classmethod
    def get(cls):
        return Orders.select()

    @classmethod
    def show(cls, id):
        return Orders.get_or_none(id)

    @classmethod
    def add(cls, user_id, status_id, payments_id, date):
        Orders.create(user_id=user_id, status_id=status_id, payments_id=payments_id, date=date)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Orders.update({key: value}).where(Orders.id == id).execute()

    @classmethod
    def delete(cls,id):
        Orders.delete_by_id(id)

    @classmethod
    def count(cls):
        count = Orders.select().count()
        return count

# Вывод за день
    @classmethod
    def report_day(cls,day):
        return Orders.select().where(Orders.date == day).count()

# Вывод за неделю
#     @classmethod
#     def report_week(cls,day):
#         day преобразовать datetime
# найти начальную дату неделю и последнюю с помощью timedelta


if __name__ == '__main__':
    # for row in OrdersController.get():
        # print(row.user_id, row.status_id, row.payments_id, row.date)
        print(OrdersController.report_day('2024-05-12'))