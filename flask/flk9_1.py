from flask import Flask
from flaskext.mysql import MySQL
app=Flask(__name__)
mysql=MySQL()

app.config["MYSQL_DATABASE_HOST"]="localhost"
app.config["MYSQL_DATABASE_USER"]="root"
app.config["MYSQL_DATABASE_PASSWORD"]="root"
app.config["MYSQL_DATABASE_DB"]="thirddb"


mysql.init_app(app)

