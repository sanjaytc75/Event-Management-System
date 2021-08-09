from flask import render_template, flash, redirect, request
from Event import app, db, bcrypt 
from Event.forms import RegistrationForm, LoginForm, FeedbackForm, BookingForm, UpdateForm, PaymentForm
from Event.models import User, Feedback, Booking, Login, Payment
from flask.helpers import url_for
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/",methods=['GET', 'POST'])
@app.route("/login.html", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@event.com' and form.password.data == 'password':
            return redirect(url_for('admin'))
        else:
            user = User.query.filter_by(email = form.email.data).first()
            if user and bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                login = Login(email=form.email.data,user_id=user.id)
                db.session.add(login)
                db.session.commit()
                return redirect(url_for('home'))
            else:
                flash("Login unsuccessful. Please check your email and password","success")
    return render_template('login.html', title='Title', form=form)

@app.route("/register.html", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/home.html")
@login_required
def home():
    return render_template('home.html')

@app.route("/form.html", methods=['GET', 'POST'])
@login_required
def form():
    form = BookingForm()
    if form.validate_on_submit():
        print("Success")
        booking = Booking(name=form.name.data, email=form.email.data, event_name=form.event_name.data, date=form.date.data, phone=form.phone.data, attendees=form.attendees.data, time=form.time.data, city=form.city.data, venue=form.venue.data, additional_requirements=form.additional_requirements.data, user_id=current_user.id)
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for('payment'))
    return render_template('form.html', title='Forms', form=form)

@app.route("/feedback.html", methods=['GET', 'POST'])
@login_required
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        feedback = Feedback(name=form.name.data, email=form.email.data, feedback=form.feedback.data, user_id=current_user.id)
        db.session.add(feedback)
        db.session.commit()
        flash("Thank you for the feedback !!","success")
    return render_template('feedback.html', title='Feedback', form=form)
    
@app.route("/payment.html", methods=['GET', 'POST'])
@login_required
def payment():
    form = PaymentForm()
    if form.validate_on_submit():
        booking = Booking.query.get_or_404(current_user.id)
        payment = Payment(name_on_card=form.name.data,card_number=form.card_number.data,expiry_date=form.expiry_date.data,cvv=form.cvv.data, user_id=current_user.id)
        db.session.add(payment)
        db.session.commit()
        flash("Payment Done !!","success")
    return render_template('payment.html', title="Payment", form=form)

@app.route("/admin.html", methods=['GET', 'POST'])
def admin():
    admin = Booking.query.all()
    form = BookingForm()
    return render_template('admin.html', title="Admin page",form=form, posts=admin)

@app.route("/admin_booking.html", methods=['GET', 'POST'])
def admin_booking():
    form = BookingForm()
    if form.validate_on_submit():
        print("Success")
        booking = Booking(name=form.name.data, email=form.email.data, event_name=form.event_name.data, date=form.date.data, phone=form.phone.data, attendees=form.attendees.data, time=form.time.data, city=form.city.data, venue=form.venue.data, additional_requirements=form.additional_requirements.data, user_id='Admin')
        db.session.add(booking)
        db.session.commit()
        return redirect(url_for('admin_booking'))
    return render_template('admin_booking.html', title='Forms', form=form)

@app.route("/admin.html/update.html/<int:booking_id>", methods=['GET', 'POST'])
def update(booking_id):
    book = Booking.query.get_or_404(booking_id)
    form = UpdateForm()
    if form.validate_on_submit():
        book.name = form.name.data
        book.email=form.email.data
        book.event_name=form.event_name.data
        book.phone=form.phone.data
        book.attendees=form.attendees.data
        book.time=form.time.data
        book.city=form.city.data
        book.venue=form.venue.data
        book.additional_requirements=form.additional_requirements.data
        db.session.commit()
        flash("Form has been updated","Success")
        return redirect(url_for('admin'))
    form.name.data = book.name
    form.email.data = book.email
    form.event_name.data = book.event_name
    form.phone.data = book.phone
    form.attendees.data=book.attendees
    form.time.data = book.time
    form.city.data=book.city
    form.venue.data=book.venue
    form.additional_requirements.data=book.additional_requirements
    return render_template('update.html', title="Admin update page",post=book,form=form)

@app.route("/admin.html/delete.html/<int:booking_id>", methods=['POST'])
def delete(booking_id):
    book = Booking.query.get_or_404(booking_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('admin'))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
