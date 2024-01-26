from flask import Flask,request,render_template

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

if __name__ == "__main__":
    app.run(debug=True)
