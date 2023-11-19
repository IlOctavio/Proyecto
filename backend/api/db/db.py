from api import app
from flask_mysqldb import MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'userad_db_proyecto'
app.config['MYSQL_PASSWORD'] ='pass123'
app.config['MYSQL_DB'] = 'db_proyecto'

mysql = MySQL(app)

class DBError(Exception):
    pass