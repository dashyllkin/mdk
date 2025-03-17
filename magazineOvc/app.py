from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from Controllers.UserController import UserController

application = Flask(__name__)
application.secret_key = 'your_secret_key'  # Секретный ключ для Flask-Login

# Инициализация Flask-Login
login_manager = LoginManager()
login_manager.init_app(application)
login_manager.login_view = 'home'

# Загрузка пользователя для Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return UserController.show(user_id)

# Главная страница (аутентификация)
@application.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        user = UserController.show_login(login)
        print(login)
        print(password)

        if UserController.auth(login, password):
            login_user(user)
            if login == 'admin':
                return redirect('/admin')
            else:
                return redirect('/client')
        else:
            print('Вы ввели неверный логин или пароль')
    return render_template('index.html')

# Маршрут для регистрации
@application.route('/registration', methods=['POST', 'GET'])
def registration():
    message = ''
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if UserController.registration(login, password):
            user = UserController.auth(login, password)
            login_user(user)
            if user.login == 'admin':
                return redirect('/admin')
            else:
                return redirect('/client')
        else:
            message = 'Такой логин уже существует'
    return render_template('register.html', message=message)

# Выход из системы
@application.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Маршрут для панели администратора
@application.route('/admin')
@login_required
def admin_panel():
    return render_template('admin.html')


# Маршрут каталога
@application.route('/catalog')
@login_required
def catalog():
    return render_template('catalog.html')


# маршрут для клиентов
@application.route('/client')
@login_required
def client():
    return render_template('client.html')

# маршрут на склад для админа
@application.route('/warehouse')
@login_required
def warehouse():
    return render_template('warehouse.html')

# маршрут на страницу заказов для админа
@application.route('/orders')
@login_required
def orders():
    return render_template('orders.html')

# маршрут на страницу отчетов для админа
@application.route('/reports')
@login_required
def reports():
    return render_template('reports.html')

if __name__ == "__main__":
    application.run(debug=True)