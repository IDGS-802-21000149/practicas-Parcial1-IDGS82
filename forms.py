from wtforms import Form, SelectField, RadioField

class resistenciaForm(Form):
    colores = [
        ("Negro", "Negro"), ("Marrón", "Marrón"), ("Rojo", "Rojo"),
        ("Naranja", "Naranja"), ("Amarillo", "Amarillo"), ("Verde", "Verde"),
        ("Azul", "Azul"), ("Violeta", "Violeta"), ("Gris", "Gris"),
        ("Blanco", "Blanco")
    ]

    tolerancias = [("dorado", "Dorado"), ("plata", "Plata")]

    color_1 = SelectField('Color 1', choices=colores)
    color_2 = SelectField('Color 2', choices=colores)
    color_3 = SelectField('Color 3', choices=colores)
    tolerancia = RadioField('Tolerancia', choices=tolerancias)
