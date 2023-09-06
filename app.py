from flask import Flask, render_template
import mysql.connector
from flask import request
cnx = mysql.connector.connect(user='satyam', password='satyam', host='127.0.0.1', database='mysql')
cnx.close()
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html')


@app.route('/add_subscriber', methods=['GET', 'POST'])
def add_subscriber():
    data = request.data
    cnx = mysql.connector.connect(user='satyam', password='satyam', host='127.0.0.1', database='mysql')
    cursor = cnx.cursor()
    insert = 'insert into subscribers (first_name,email) values(%s,%s);'
    cursor.execute(insert, data)
    cnx.close()


if __name__ == '__main__':
    app.run()
