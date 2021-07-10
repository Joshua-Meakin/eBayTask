from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField

from wtforms import validators, ValidationError

class SubmitForm(FlaskForm):
    p_postcode= TextField("Pickup postcode",[validators.Required("Please enter your pickup postcode.")])
    d_postcode= TextField("Delivery postcode",[validators.Required("Please enter your delivery postcode.")])
    vehicle = SelectField('Vehicle', choices = [('Bicycle', 'Bicycle'), 
                                                ('Motorbike', 'Motorbike'), 
                                                ('Parcel car', 'Parcal car'),
                                                ('Small van', 'Small van'),
                                                ('Large van', 'Large van')])
    submit = SubmitField("Calculate the price")
