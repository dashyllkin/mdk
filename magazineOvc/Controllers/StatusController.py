from Models.Statuses import *

class StatusController:
    # Метод вывода всех записей таблицы Статусы
    @classmethod
    def get(cls):
        return Statuses.select()
    @classmethod
    def show(cls,id):
        return Statuses.get_or_none(id)


if __name__ == "__main__":
    for row in StatusController.get():
        print(row.id, row.status_name)