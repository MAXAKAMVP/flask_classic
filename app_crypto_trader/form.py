from flask_wtf import FlaskForm
from wtforms import DateField,StringField,FloatField,SubmitField
from wtforms.validators import DataRequired,Length,ValidationError
from time import strftime

class Form_inputs(FlaskForm):
    date_select = strftime(" %Y/%m/%d")
    hora_select = strftime(" %H:%M:%S")

    base = StringField('Base', validators=[DataRequired("")])
    quote = StringField('Quote', validators=[DataRequired("")])
    amount = FloatField('Amount_base', validators=[DataRequired("El monto es requirido, debe ser mayor a 0")])
    submit = SubmitField('Submit')