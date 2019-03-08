# IMPORTANDO BIBLIOTECAS
from historico import *
from flask import Flask, url_for, redirect, request, render_template

# INSTANCIANDO A APP FLASK
app = Flask(__name__)

# ROTA PARA /
@app.route('/')
def princioal():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login = request.form.get('login')
        senha = request.form.get('senha')

        # verificar senha
        if get_login(login, senha):
            return render_template('oi.html', nome=login, disciplinas=get_disciplinas(login))
        else:
            return render_template('index.html', erro='Login/Senha incorretos')
    else:
        return render_template('index.html', erro='Método incorreto. Use POST!')

# RODANDO O APP
if __name__ == '__main__':
    app.run(debug=True)