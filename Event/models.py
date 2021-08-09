from Event import db, login_manager
from flask_login import  UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    login = db.relationship('Login', backref='login', lazy=True)

    def __repr__(self):  #How object is printed when we print it .
        return f"User('{self.name}','{self.email}')"

class Login(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    booking = db.relationship('Booking', backref='booking', lazy=True)
    payment1 = db.relationship('Payment', backref='payment1', lazy=True)
    feedback1 = db.relationship('Feedback', backref='feedback1', lazy=True)
    delete_booking = db.relationship('log_delete', backref='delete_booking', lazy=True)

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(30), nullable=False) 
    feedback = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('login.user_id'), nullable=False)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(30), nullable=False)
    event_name = db.Column(db.String(30), nullable = False)
    city = db.Column(db.String(30), nullable = False)
    venue = db.Column(db.String(30), nullable=True)
    date = db.Column(db.String(30), nullable = False)
    phone = db.Column(db.String(30), nullable = False)
    attendees = db.Column(db.Integer, nullable = False)
    time = db.Column(db.Time, nullable = False)
    additional_requirements = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('login.user_id'), nullable=False)

    def __repr__(self):  #How object is printed when we print it .
        return f"User('{self.name}','{self.email}')"

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name_on_card = db.Column(db.String(30),nullable=False)
    card_number = db.Column(db.String(30),nullable=False)
    expiry_date = db.Column(db.String(30), nullable = False)
    cvv = db.Column(db.String(30), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('login.user_id'), nullable=False)
    
class log_delete(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    email = db.Column(db.String(30), nullable=False)
    event_name = db.Column(db.String(30), nullable = False)
    city = db.Column(db.String(30), nullable = False)
    venue = db.Column(db.String(30), nullable=True)
    date = db.Column(db.String(30), nullable = False)
    phone = db.Column(db.String(30), nullable = False)
    attendees = db.Column(db.Integer, nullable = False)
    time = db.Column(db.Time, nullable = False)
    additional_requirements = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('login.user_id'), nullable=False)

    def __repr__(self):  #How object is printed when we print it .
        return f"User('{self.name}','{self.email}')"