from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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
