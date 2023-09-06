from flask import Flask
import mysql.connector

cnx = mysql.connector.connect(user='satyam', password='satyam',host='127.0.0.1',database='mysql')
cnx.close()
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
