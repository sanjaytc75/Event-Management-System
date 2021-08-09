from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms import validators
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from Event.models import User
from wtforms.fields.html5 import DateField
from wtforms_alchemy import PhoneNumberField
from wtforms_components import TimeField
import phonenumbers
from _datetime import datetime

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('The email already exists')

class LoginForm(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class FeedbackForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(), Email()])
    feedback = TextAreaField('Feedback',validators=[DataRequired()])
    submit = SubmitField('Submit')
    
class BookingForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(), Email()])
    event_name = StringField('Event Name', validators=[DataRequired()])
    date = DateField("Date",format='%Y-%m-%d')
    phone = StringField('Phone', validators=[DataRequired()])
    attendees = IntegerField('Attendees',validators=[DataRequired()])
    time = TimeField('Time', format='%H:%M')
    city = StringField('City', validators=[DataRequired()])
    venue = StringField('venue')
    additional_requirements = TextAreaField('Additional Requirements',validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_phone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')
    
class UpdateForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    email = StringField('Email',validators=[DataRequired(), Email()])
    event_name = StringField('Event Name', validators=[DataRequired()])
    date = DateField("Date",format='%Y-%m-%d')
    phone = StringField('Phone', validators=[DataRequired()])
    attendees = IntegerField('Attendees',validators=[DataRequired()])
    time = TimeField('Time', format='%H:%M')
    city = StringField('City', validators=[DataRequired()])
    venue = StringField('venue')
    additional_requirements = TextAreaField('Additional Requirements',validators=[DataRequired()])
    submit = SubmitField('Submit')

    def validate_phone(self, phone):
        try:
            p = phonenumbers.parse(phone.data)
            if not phonenumbers.is_valid_number(p):
                raise ValueError()
        except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
            raise ValidationError('Invalid phone number')

class PaymentForm(FlaskForm):
    name = StringField('Name',validators=[DataRequired()])
    card_number = StringField('Card Number',validators=[DataRequired(),Length(min=16,max=16)])
    expiry_date = DateField('Date',format='%Y-%m-%d')
    cvv = StringField('CVV', validators=[DataRequired(), Length(3,3)])
    submit = SubmitField('Submit')
