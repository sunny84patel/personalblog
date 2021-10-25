
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWPORD']=""
app.config['MYSQL_DB']='blogger'
mysql= SQLAlchemy(app)


class Contacts(mysql.Model):
    sno = mysql.Column(mysql.Integer, primary_key=True)
    name = mysql.Column(mysql.String(80), nullable=False)
    email = mysql.Column(mysql.String(12), nullable=False)
    phone = mysql.Column(mysql.String(120),  nullable=False)
    date = mysql.Column(mysql.String(12) , nullable=True)
    msg  = mysql.Column(mysql.String(20),  nullable=False)




@app.route("/")
def home():
    return render_template('index.html')

     
@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/post1")
def post():
    return render_template('post1.html')


@app.route("/contact", methods = ['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        name = details['name']
        email = details['email']
        phone = details['phone']
        date= details['date']
        msg= details['msg']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO blogger(name, email, phone, msg) VALUES (%s, %s ,%s ,%s, %s)", (name, email ,phone ,date ,msg))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('contact.html')


if(__name__=='__main__'):
  app.run(debug=True)