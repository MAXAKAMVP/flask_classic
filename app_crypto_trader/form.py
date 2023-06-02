#from app_crypto_trader.models_db import Db_data
#from datetime import datetime
#from app_crypto_trader.models import Api_data
"""
class Form:
    date = datetime.now().date()
    time = datetime.now().strftime("%H:%M:%S")
    base = request.form['base']
    quote = request.form['quote']
    base_amount = int(request.form['base_amount'])
    pu = Api_data.get_rate(base, quote)
    acquired_amount = Api_data.get_amount_acquired(pu, base_amount)
    data = [date, time, base, base_amount, quote, acquired_amount]
    def form_calc(self):
        return self.data
    def form_confirm(self):
        return self.data
"""
# Validador de formulario
"""
def form_validator(data_form):
    errors = []
    
    if data_form["base"] == "":
        errors.append("Debes seleccionar una moneda base")

    if  data_form["quote"] == "" or data_form["base_amount"] == 0:
        errors.append("Debes introducir una cantidad a gastar")

    if data_form["base"] == "":
        errors.append("Debes seleccionar una moneda a comprar")
        prueba_cantidad = .cantidad_crypto()
        try:
            q_from = prueba_cantidad[data_form["from_select"]]
            if float(data_form["quantity"]) > float(q_from):
                errors.append("Su cartera es insuficiente para esta transacción")
        except:
            errors.append("Introduce tipo de cryptomoneda o moneda")
    
    return errors
"""