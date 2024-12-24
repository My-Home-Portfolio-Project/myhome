from flask import Flask, render_template, request, redirect, url_for, flash
from flask_bcrypt import Bcrypt
from models import User, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'
bcrypt = Bcrypt(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        username = request.form['username']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')

        # Check if the user already exists
        existing_user = session.query(User).filter_by(email=email).first()
        if existing_user:
            flash('Email already registered!', 'danger')
            return redirect(url_for('register'))

        # Add the user to the database
        new_user = User(email=email, username=username, password=password)
        session.add(new_user)
        session.commit()
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Authenticate user
        user = session.query(User).filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password!', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return "Welcome to your dashboard!"

if __name__ == '__main__':
    app.run(debug=True)
 