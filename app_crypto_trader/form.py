from flask_wtf import FlaskForm
from wtforms import DateField,StringField,FloatField,SubmitField
from wtforms.validators import DataRequired,Length,ValidationError
from time import strftime

class Form_inputs(FlaskForm):
    date_select = strftime(" %d/%m/%Y")
    hora_select = strftime(" %H:%M:%S")

    base = StringField('From', validators=[DataRequired("")])
    quote = StringField('Quote', validators=[DataRequired("")])
    amount = FloatField('Amount', validators=[DataRequired("El monto es requirido, debe ser mayor a 0")])
    submit = SubmitField('Submit')