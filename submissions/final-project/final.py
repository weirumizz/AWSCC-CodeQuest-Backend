import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db = SQLAlchemy(app)

class Password(db.Model):
    __tablename__ = 'passwords' 
    id = db.Column(db.Integer, primary_key=True)
    website = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

@app.route('/')
def home():
    with app.app_context():
        db.create_all() 
    passwords = Password.query.all()
    return render_template('index.html', passwords=passwords)

@app.route('/add', methods=['POST'])
def add():
    website = request.form['website']
    email = request.form['email']
    password = request.form['password']
    
    new_password = Password(website=website, email=email, password=password)
    db.session.add(new_password)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/update/<int:password_id>', methods=['POST'])
def update_password(password_id):
    password = Password.query.get_or_404(password_id)
    password.website = request.form['website']
    password.email = request.form['email']
    password.password = request.form['password']
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:password_id>', methods=['POST'])
def delete(password_id):
    password = Password.query.get_or_404(password_id)
    db.session.delete(password)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
