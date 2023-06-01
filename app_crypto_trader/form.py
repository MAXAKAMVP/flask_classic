#from flask_wtf import FlaskForm
#from wtforms import StringField, FloatField, SubmitField, Form
#from wtforms.validators import DataRequired
#from time import strftime
"""
class Form_input(Form):
    base = StringField('Moneda De Entrada', validators=[DataRequired()])
    quote = StringField('Moneda De Salida', validators=[DataRequired()])
    amount_base = FloatField('Cantidad', validators=[DataRequired()])
    amount_quote = FloatField('Cantidad', validators=[DataRequired()])
    submit = SubmitField('Submit')

    date = strftime("%Y/%m/%d") 
    time = strftime("%H:%M:%S")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.date_select.data = strftime("%Y/%m/%d")
        self.time_select.data = strftime("%H:%M:%S")
"""