import os
import subprocess
from MySQLdb import connect
from flask import Flask

app = Flask(__name__)
mysql_host = os.environ.get("MYSQL_HOST")
mysql_user = os.environ.get("MYSQL_USER")
mysql_password = os.environ.get("MYSQL_PASSWORD")
mysql_db_name = os.environ.get("MYSQL_DATABASE_NAME")


@app.route("/")
def index():
    return "Hello review"


@app.route("/units")
def units():
    content = "<h1>host is: {0}</h1>".format(subprocess.check_output("hostname"))
    return content


@app.route("/envs")
def envs():
    response = ""
    for env, value in os.environ.items():
        response = "{}<b>{}</b> = {} <br />".format(response, env, value)
    return response


@app.route("/db")
def test_connection():
    try:
        db = connect(host=mysql_host, user=mysql_user,
                     passwd=mysql_password, db=mysql_db_name)
        msg = "Successfuly connect into database"
        db.close()
    except Exception:
        msg = "Got error while connecting with database"
    msg += "<h1>host is: {0}</h1>".format(subprocess.check_output("hostname"))
    return msg


if __name__ == "__main__":
    app.debug = True
    app.run()
