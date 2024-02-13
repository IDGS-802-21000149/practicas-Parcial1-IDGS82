from flask import Flask,request,render_template
import math
import forms 


app=Flask(__name__)

@app.route("/calculadora")
def calculadora():
    return render_template("calculadora.html")

@app.route("/operaciones",methods=["GET","POST"])
def operaciones():
    if request.method=="POST":
     operacion=request.form.get("operacion")
     n1=request.form.get("n1")
     n2=request.form.get("n2")
     if operacion == "Suma":
         resultado = str(int(n1)+int(n2))
     elif operacion == "Resta": 
          resultado = str(int(n1)-int(n2))
     elif operacion == "Multiplicacion": 
          resultado = str(int(n1)*int(n2))
     elif operacion == "Division": 
          resultado = str(int(n1)/int(n2))
    return render_template("calculadora.html", resultado=resultado)


@app.route("/dosPuntos", methods=["GET", "POST"])
def dos_puntos():
    if request.method == "POST":
        x1_str = request.form.get("x1")
        x2_str = request.form.get("x2")
        y1_str = request.form.get("y1")
        y2_str = request.form.get("y2")

        if x1_str and x2_str and y1_str and y2_str:
            x1, x2, y1, y2 = float(x1_str), float(x2_str), float(y1_str), float(y2_str)

            distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            resultado = f"La distancia entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {distancia}"
        else:
            resultado = "Por favor, complete todos los campos."

        return render_template("pendiente.html", resultado=resultado)

    return render_template("pendiente.html")



def calcular_resistencia(colores, tolerancia):
    # Diccionario que asocia colores con sus valores numéricos
    valores = {
        "Negro": 0, "Marrón": 1, "Rojo": 2, "Naranja": 3,
        "Amarillo": 4, "Verde": 5, "Azul": 6, "Violeta": 7,
        "Gris": 8, "Blanco": 9
    }

    # Obtiene el valor numérico de los colores y calcula la resistencia
    valor_resistencia = int(str(valores[colores[0]]) + str(valores[colores[1]]))
    valor_resistencia *= 10 ** valores[colores[2]]

    return valor_resistencia


def calcular_tolerancia(valor_resistencia, tolerancia):
    # Asocia colores de tolerancia con porcentajes de tolerancia
    tolerancia_porcentaje = {
        "dorado": 5, "plata": 10
    }

    tolerancia_valor = valor_resistencia * tolerancia_porcentaje[tolerancia] / 100
    valor_maximo = valor_resistencia + tolerancia_valor
    valor_minimo = valor_resistencia - tolerancia_valor

    return valor_maximo, valor_minimo


@app.route("/resistencias", methods=["GET", "POST"])
def resistencia():
    form = forms.resistenciaForm(request.form)
    if request.method == 'POST' and form.validate():
        colores = [form.color_1.data, form.color_2.data, form.color_3.data]
        tolerancia = form.tolerancia.data

        valor_resistencia = calcular_resistencia(colores, tolerancia)
        valor_maximo, valor_minimo = calcular_tolerancia(valor_resistencia, tolerancia)

        resultados = {
            'color_1': form.color_1.data,
            'color_2': form.color_2.data,
            'color_3': form.color_3.data,
            'tolerancia': form.tolerancia.data,
            'valor_resistencia': valor_resistencia,
            'valor_maximo': valor_maximo,
            'valor_minimo': valor_minimo
        }

        return render_template("resistencias.html", form_resistencia=form, resultados=resultados)
    return render_template("resistencias.html", form_resistencia=form)


if __name__ == "__main__":
    app.run(debug=True)