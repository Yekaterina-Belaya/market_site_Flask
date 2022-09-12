from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '21b99fc4cc89fdb28bdb0636'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

from market import routes

'''create db (another way): in terminal 
python --> from market import db --> db.create_all()
next create items via terminal
>>> from market import Item
>>> item1 = Item(name="IPhone 10", barcode="768954638567", price=500, description="IPhone model 10 by Apple, original")    
>>> db.session.add(item1)
>>> db.session.commit()
>>> Item.query.all()
[<Item 1>]
'''
