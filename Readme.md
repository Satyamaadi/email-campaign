Running this App - 

For running this app - you need to install mysql server 8.0x,
python 3.9 ,an IDE (i used pycharm) if you dont have ide then also it can run (diff way - not explained here)

first you have to create the database with tables given in subscribers.sql file,
then we have to get python-connector-mysql package to connect python BE to DB,
after the connection is done, we can then start the app by running app.py file, an html page 
will open, and then you can perform all the ops as required.


This app has two components -
1. Backend (python + mysql)
2. Frontend (HTML + CSS)

BackEnd - Written in python, uses flask framework to serve user requests.
Backend in collaboration with mysql db can serve all the use cases mentioned like adding subscribers, soft deleting the subscribers
,sending email campaigns to multiple users although here i am sending only to one customer.

FrontEnd - Written in HTML using some CSS to design, it is written using <form> to send request to server and get results from server.
It acts as user interface to the customer.

API Descriptions - 

I have used flask framework to make BE swift and fast.
The database that i have used is MySQL Server 8.04.
SMTP library has also been used to send emails.

1. def home_page() - This is the home page route - user when opens the app, gets home page returned to him ,which is an html file.

2. add_subscriber() - This route is used to add subscriber to database using MySQL DB, from FrontEnd - the first name and email-id of customer is sent
and it gets added to the database.

3. remove_subscriber() - This route is used to soft delete the user, by making is_active=false for the concerned email id 

4. send_simple_message() - This route is used to send customised email campaigns to multiple users, but for now it sends only to one email - which is mine.
the email has components like preview text, subject, article url, html content ,publish date. 
So all these components are combined and a customised email is send to all the users.
It uses mailgun sandbox and domain to send emails via smtp protocol, we login to sandbox server using username and password and then send then mail.


** Note - All these methods are supposed to be written in different .py files and then called from app.py, that means all these
methods are each one API ,which should be written in different file, but for the sake of understanding i have added all these in app.py only.