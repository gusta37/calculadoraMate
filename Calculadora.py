from flask import Flask, request, render_template, session, redirect, url_for
import math

app = Flask(__name__)
app.secret_key = "mi_clave_secreta"

def calcular_angulo(d, h):
    theta = math.atan(2 * h / d)
    angulo_en_grados = math.degrees(theta)
    return angulo_en_grados

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "accion" in request.form:
            accion = request.form["accion"]
            if accion == "calcular":
                distancia_str = request.form.get("distancia")
                altura_str = request.form.get("altura")
                
                # Verificar si los campos están vacíos
                if not distancia_str or not altura_str:
                    session["resultado"] = "No ingresaste datos. Por favor, completa todos los campos."
                else:
                    try:
                        distancia = float(distancia_str)
                        altura = float(altura_str)
                        angulo_optimo = calcular_angulo(distancia, altura)
                        session["resultado"] = f"El ángulo óptimo es de: {angulo_optimo:.2f} grados"
                    except ValueError:
                        session["resultado"] = "Por favor, ingresa valores numéricos válidos."
            elif accion == "borrar":
                session.pop("resultado", None)  # Elimina el resultado de la sesión
                return redirect(url_for("index"))  # Redirige a la página de inicio para limpiar el formulario
        session.modified = True
    return render_template("index.html", resultado=session.get("resultado"))

if __name__ == "__main__":
    app.run()

