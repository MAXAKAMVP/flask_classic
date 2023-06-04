
def form_validator(data_form):
    errors = []
    if data_form["base"] == "0":
        errors.append("Debe seleccionar una moneda base")
    if data_form["quote"] == "0":
        errors.append("Debe seleccionar una moneda quote")
    if data_form["base_amount"] == "":
        errors.append("Debe introducir una cantidad a gastar")
    return errors
