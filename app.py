from flask import Flask, render_template, request, redirect
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

USERS = {
    "": ""
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html', error=None)

@app.route('/acesso', methods=['POST'])
def acesso():
    username = request.form['username']
    password = request.form['password']

    if username in USERS and USERS[username] == password:
        return redirect('/servicos')
    else:
        logging.warning(f'Tentativa de login inválido: {username}')
        return render_template('login.html', error="Usuário ou senha incorretos")

@app.route('/servicos')
def servicos():
    return render_template('servicos.html')


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        email = request.form['email']
        nome = request.form['nome']
        senha = request.form['senha']
        endereco = request.form['endereco']
        datadenascimento = request.form['data de nascimento']
        cpf = request.form['cpf']



        return redirect(url_for('sucesso'))

    return render_template('cadastro.html')

@app.route('/sucesso')
def sucesso():
    return "Cadastro realizado com sucesso!"

if __name__ == '__main__':
    app.run(debug=True)
