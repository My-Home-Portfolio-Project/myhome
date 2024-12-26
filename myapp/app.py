#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
 
app = Flask(__name__)
app.secret_key = 'dontfuckwithme!'  # Replace with a secure secret key
 
# Configure SQLAlchemy with MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:FlavianLeonar2003$@localhost/myhome'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"User('{self.email}', '{self.name}', '{self.contact}')"

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        contact = request.form['contact']

        # Check if user already exists
        if User.query.filter_by(email=email).first():
            flash('Email already registered. Please log in.', 'danger')
            return redirect(url_for('register'))

        # Hash the password before saving
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

        # Save user to the database
        new_user = User(email=email, password=hashed_password, name=name, contact=contact)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Find the user by email
        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            # Store user session
            session['user_id'] = user.id
            session['user_name'] = user.name
            flash(f'Welcome, {user.name}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Please log in to access this page.', 'danger')
        return redirect(url_for('login'))
    return f"Welcome to your dashboard, {session['user_name']}!"

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
 