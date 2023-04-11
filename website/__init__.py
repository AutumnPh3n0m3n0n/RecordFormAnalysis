from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager
import mysql.connector

formsDB = mysql.connector.connect(
    host='localhost',
    user='root',
    password='P0rtl4nd_0r3gOn',
    port='3306',
    database='forms'
)

myCursor = formsDB.cursor(buffered=True)

myCursor.reset()

myCursor.execute('select * from BankAccountForm')
myCursor.execute('select * from CreditCardForm')
myCursor.execute('select * from MedicalRecordsForm')

db = SQLAlchemy()
DB_NAME = "formsDB"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'UrM0mW0rkzF0rM3'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:P0rtl4nd_0r3gOn@localhost/forms'
    db.init_app(app)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note, BankAccountForm, CreditCardForm, MedicalRecordsForm

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')
