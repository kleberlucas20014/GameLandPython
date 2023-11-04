from flask import Flask, render_template , request, redirect, session, flash, url_for


class Jogo:
    def __init__(self, nome, categoria, console):
       self.nome = nome
       self.categoria = categoria
       self.console = console

       jogo1 = Jogo('tetris', 'puzzle', 'atari')
       jogo2 = Jogo('god of war', 'rack n slash', 'ps2')
       jogo3 = Jogo('Mortal Kombat', 'fight', 'ps2')
       lista_jogos = [jogo1, jogo2, jogo3]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Bruno","BD","root")
usuario2 = Usuario("teste","teste","root")

usuarios = {usuario1.nickname : usuario1,
            usuario2.nickname : usuario2}

app = Flask(__name__)
app.secret_key = 'toor'

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista_jogos)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session ['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html',titulo='novo jogo')

@app.route('/criar', methods =['POST',])
def criar():
   nome = request.form['nome']
   categoria = request.form['categoria']
   console = request.form['console']
   jogo = Jogo('nome', 'categoria', 'console')
   lista_jogos.append(jogo)
   return (redirect (url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + 'logado com sucesso')
            proxima_pagina = request.form('proxima')
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com susseso!')
    return redirect(url_for('index'))


app.run(debug=True)




