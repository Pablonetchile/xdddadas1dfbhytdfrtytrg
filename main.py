from flask import Flask, render_template
import random

app = Flask(__name__)
facts_list = ["Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, de modo que pasemos el mayor tiempo posible viendo contenidos.", 
            "Según un estudio realizado en 2018, más del 50 de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.", 
            "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas.", 
            "El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna."]

@app.route('/')
def a():
    return render_template('index.html')
@app.route('/rl')
def b():
    return render_template('rl.html', lista_de_infartos=random.choice(facts_list))

app.run(debug=True)