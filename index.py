# Portfólio in Flask
# by geanclm in 14/04/2022 at 08:15h
from flask import Flask, render_template

# --- bloco para apresentar a data atual - start
import time, random
from datetime import datetime, date
from pytz import timezone
# Variables date
registro_data_e_hora_completo = time.ctime()
hoje = datetime.now()
fuso_horario = timezone("America/Sao_Paulo")
data_e_hora = hoje.astimezone(fuso_horario)
agora = data_e_hora.strftime("%A %B %d/%m/%Y %H:%M"+"h")
# --- bloco para apresentar a data atual - end

app = Flask(__name__)

@app.route('/')

def homepage():
    marca = 'geanclm'
    return render_template('homepage.html',
                           marca=marca, agora=agora)

@app.route('/contatos')
def contatos():
    return render_template('contatos.html')

@app.route('/usuarios/<nome_usuario>')
def usuarios(nome_usuario):
    return render_template('usuarios.html',
                           nome_usuario=nome_usuario)

# site no ar
if __name__ == "__main__":
    app.run(debug=True)

# servidor do Heroku