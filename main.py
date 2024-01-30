from flask import Flask,request,render_template
import math

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


if __name__ == "__main__":
    app.run(debug=True)
