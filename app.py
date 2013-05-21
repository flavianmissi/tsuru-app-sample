import os
from flask import Flask
from MySQLdb import connect


app = Flask(__name__)
mysql_host = os.environ.get("MYSQL_HOST")
mysql_user = os.environ.get("MYSQL_USER")
mysql_password = os.environ.get("MYSQL_PASSWORD")
mysql_db_name = os.environ.get("MYSQL_DATABASE_NAME")

@app.route("/")
def index():
    return "Hello world!"

@app.route("db")
def test_connection():
    try:
        db = connect(host=mysql_host, user=mysql_user,
                     passwd=mysql_password, db=mysql_db_name)
        msg = "Successfuly connect into database"
    except Exception as e:
        msg = "Got error while connecting with database"
    return msg

if __name__ == "__main__":
    app.run()
