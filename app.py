from email.mime.multipart import MIMEMultipart

from flask import Flask, render_template
import mysql.connector
from flask import request
import requests
import smtplib
from email.mime.text import MIMEText

cnx = mysql.connector.connect(user='satyam', password='satyam', host='127.0.0.1', database='mysql')
cnx.close()
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('home.html')


@app.route('/add_subscriber', methods=['GET', 'POST'])
def add_subscriber():
    a = request.form['fname']
    b = request.form['email']
    data = (a, b)
    cnx = mysql.connector.connect(user='satyam', password='satyam', host='127.0.0.1', database='mysql')
    cursor = cnx.cursor()
    insert = 'insert into subscribers (first_name,email) values(%s,%s);'
    cursor.execute(insert, data)
    cnx.commit()
    cursor.close()
    cnx.close()
    return {'statuscode': 200}


@app.route('/unsubscribe', methods=['GET', 'POST'])
def remove_subscriber():
    a = request.form['email']
    # a = (a)
    cnx = mysql.connector.connect(user='satyam', password='satyam', host='127.0.0.1', database='mysql')
    cursor = cnx.cursor()
    up = "update subscribers set is_active = false where email = '{}';"
    cursor.execute(up.format(a))
    cnx.commit()
    cursor.close()
    cnx.close()
    return {'statuscode': 200}


@app.route('/send_email')
def send_simple_message():
    #msg = MIMEText('Testing some Mailgun awesomness')
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Hello"
    msg['From'] = "foo@sandboxe31f460a7b0d4ce8a327a5aee444d8c7.mailgun.org"
    msg['To'] = "satyamshikhar@gmail.com"
    html = """
    <html>
      <head></head>
      <body>
        <p>Hi!<br>
           How are you?<br>
           Here is the <a href="http://www.python.org">link</a> you wanted.
        </p>
      </body>
    </html>
    """
    text=''
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    s = smtplib.SMTP('smtp.mailgun.org', 587)

    s.login('postmaster@sandboxe31f460a7b0d4ce8a327a5aee444d8c7.mailgun.org', '18be4751d126ff1317ab5f7e255c6c82-7ca144d2-004b0108')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
    return {'statuscode': 200}


if __name__ == '__main__':
    app.run()
