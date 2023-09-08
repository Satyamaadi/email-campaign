from email.mime.multipart import MIMEMultipart
import os
from flask import Flask, render_template
import mysql.connector
from flask import request
import requests
import smtplib
from email.mime.text import MIMEText

cnx = mysql.connector.connect(user=os.getenv('USER'), password=os.getenv('PASSWORD'), host=os.getenv('HOST'), database=os.getenv('DATABASE'))
cnx.close()
app = Flask(__name__)


@app.route('/')
def home_page():  # put application's code here
    return render_template('home.html')


@app.route('/add_subscriber', methods=['GET', 'POST'])
def add_subscriber():
    a = request.form['fname']
    b = request.form['email']
    data = (a, b)
    cnx = mysql.connector.connect(user=os.getenv('USER'), password=os.getenv('PASSWORD'), host=os.getenv('HOST'),
                                  database=os.getenv('DATABASE'))
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
    cnx = mysql.connector.connect(user=os.getenv('USER'), password=os.getenv('PASSWORD'), host=os.getenv('HOST'),
                                  database=os.getenv('DATABASE'))
    cursor = cnx.cursor()
    up = "update subscribers set is_active = false where email = '{}';"
    cursor.execute(up.format(a))
    cnx.commit()
    cursor.close()
    cnx.close()
    return {'statuscode': 200}


@app.route('/send_email',methods=['POST', 'GET'])
def send_simple_message():
    # msg = MIMEText('Testing some Mailgun awesomness')
    sub = request.form['subject']
    prev_txt = request.form['preview']
    art_url = request.form['article_url']
    html_cont = request.form['html_cont']
    plain_text = request.form['plain_text']
    pub_date = request.form['pub_date']
    msg = MIMEMultipart('alternative')
    msg['Subject'] = sub
    msg['From'] = "foo@sandboxe31f460a7b0d4ce8a327a5aee444d8c7.mailgun.org"
    msg['To'] = "satyamshikhar@gmail.com"
    html = """
    <html>
      <head></head>
      <body>
        <h1>XX-article_url-XX</h1>
        XX-html_cont-XX
        <p>XX-pub_date-XX</p>
      </body>
    </html>
    """
    html = html.replace('XX-article_url-XX',art_url).replace('XX-html_cont-XX',html_cont).replace('XX-pub_date-XX',pub_date)
    text = prev_txt + ' '  + plain_text
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    s = smtplib.SMTP('smtp.mailgun.org', 587)

    s.login(os.getenv('MAIL_USER'),os.getenv('MAIL_PWD'))
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()
    return {'statuscode': 200}


if __name__ == '__main__':
    app.run()
