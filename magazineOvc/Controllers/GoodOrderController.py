from Models.GoodOrder import Good_Orders
from Models.Goods import Goods


class GoodOrderController:
    @classmethod
    # вывод записей
    def get(cls):
        return Good_Orders.select()

    @classmethod
    # вывод записи по айди
    def show(cls,id):
        return Good_Orders.get_or_none(id)

    @classmethod
    # добавление
    def add(cls,order_id, good_id):
        Good_Orders.create(order_id=order_id,good_id=good_id)

    @classmethod
    # удаляем запись
    def delete(cls,id):
        Goods.delete_by_id(id)

    @classmethod
    # обновление записи
    def update(cls,id, **filds):
        for key, value in filds.items():
            Good_Orders.update({key:value}).where(Good_Orders.id == id).execute()

if __name__ == "__main__":
    for row in GoodOrderController.get():
        print(row.id, row.order_id, row.good_id)