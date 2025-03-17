from Models.Goods import *

class GoodsController:
    @classmethod
    # вывод всех записей
    def get(cls):
        return Goods.select()
    @classmethod
    # вывод одной азписи
    def show(cls,id):
        return Goods.get_or_none(id)

    @classmethod
    # добавление
    def add(cls,name, cost, quantity, description):
        Goods.create(name=name, cost=cost, quantity=quantity, description=description)

    @classmethod
    def update(cls,id, **filds):
        for key, value in filds.items():
            Goods.update({key: value}).where(Goods.id == id).execute()

    @classmethod
    def delete(cls,id):
        Goods.delete().where(Goods.id == id).execute()

    @classmethod
    # считаем сумму
    def count(cls,id):
        try:
            return GoodsController.show(id).quantity
        except Exception as error:
            print(f"Ошибка: {error}")
            return None
        # if Goods.get_or_none(id) is None:
        #     return None
        # else:
        #     return Goods.get_or_none(id).quantity


if __name__ == "__main__":
    # GoodsController.add('AirPods', '13000.00', '20', 'Лучшие наушники за свою цену')
    # GoodsController.update(21, cost = 70000.00, quantity = 40)
    # GoodsController.delete(22)
    # for Goods in GoodsController.get():
    #     print(Goods.id, Goods.name, Goods.cost, Goods.quantity, Goods.description)
    print(GoodsController.count(1))