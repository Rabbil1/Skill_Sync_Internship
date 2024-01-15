from flask import Flask, request, render_template, redirect, session
from flask_sqlalchemy import SQLAlchemy
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
app.secret_key = 'secret_key'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self, email, password, username):
        self.email = email
        self.username = username
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # handle request
        errors = []
        username = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if not user:
            new_user = User(username=username,email=email, password=password)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/login')
        
        else:
            errors.append('Email already exists')
            return render_template('register.html', errors=errors)

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        errors = []
        email = request.form['email']
        password = request.form['password']

        if not email:
            errors.append('Please enter the email')

        if not password:
            errors.append('please enter password')

        if errors:
            return render_template('login.html', errors=errors)

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            session['username'] = user.username
            session['email'] = user.email
            session['password'] = user.password
            return redirect('/dashboard')
        else:
            errors.append('Invalid Login Credentials')
            return render_template('login.html', errors=errors)
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if session['username']:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('dashboard.html', user=user)
    
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)