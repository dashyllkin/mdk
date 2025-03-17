

from Models.Users import *
from bcrypt import hashpw, gensalt, checkpw

class UserController:

    @classmethod
    def get(cls):
        return Users.select()

    @classmethod
    def show(cls,id):
        return Users.get_or_none(id)

    @classmethod
    def add(cls, login, password, roles_id):
        Users.create(login=login, password=password, roles_id=roles_id)

    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Users.update({key: value}).where(Users.id == id).execute()
    @classmethod
    def delete(cls,id):
        Users.delete().where(Users.id==id).execute()

    @classmethod
    def registration(cls,login,password):
        try:
            password= hashpw(password.encode('utf-8'),gensalt())
            Users.create(login=login,password=password,role_id=3)
        except Exception as error:
            print(error)
            return False

    # @classmethod
    # def auto(cls,login,password):
        # if Users.get_or_none(Users.login == login) != None:
            # hspassword = Users.get_or_none(Users.login == login).password

            # if Users.get_or_none(Users.login == login).password == password:
            # if checkpw(password.encode('utf-8'), hspassword.encode('utf-8')):
                # return True
            # return False
    @classmethod
    def auth(cls,login,password):
         if Users.get_or_none(Users.login==login) !=None:
             hspassword =Users.get_or_none(Users.login==login).password

             if checkpw(password.encode('utf-8'), hspassword.encode('utf-8')):
                return True
         return False


    @classmethod
    def show_login(cls,login):
        return Users.get_or_none(Users.login==login)



if __name__ == "__main__":
    for row in UserController.get():
        print(row.id, row.login, row.password, row.roles_id)

    # UserController.registration('admin2', '111111')
