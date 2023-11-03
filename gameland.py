from flask import Flask, render_template , request, redirect, session, flash, url_for


class jogo:
    def __init__(self,nome,categoria,console):
       self.nome = nome
       self.categoria = categoria
       self.console = console

       jogo1 = jogo('tetris', 'puzzle', 'ataria')
       jogo2 = jogo('god of war', 'rack n slash', 'ps2')
       lista = (jogo1,jogo2)

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = nickname

usuario1 = Usuario("Bruno","BD","root")
usuario2 = Usuario("teste","teste","root")

usuarios = {usuario1.nickname : usuario1,
            usuario2.nickname : usuario2}

app = Flask(__name__)
app.secret_key = 'toor'

@app.route('/')
def index():

    return render_template('lista.html', titulo='jogos',jogos= lista)

@app.route('/novo')
def novo():
    if 'usuario_logago' not in session or session ['usuario_logado'] == None:
        return redirect(url_for('/login', proxima=url_for('novo')))
    return render_template('novo.html',titulo = 'novo jogo')

@app.route('/criar', methods =['POST',])
def criar():
   nome = request.form['nome']
   categoria = request.form['categoria']
   console = request.form['console']
   jogo = jogo('nome','categoria','console')
   lista.append(jogo)
   return redirect (url_for('index'))

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuario:
        usuario = usuarios[request.form['usuario']]
        if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + 'usuario logado com sucesso')
            proxima_pagina = request.form('proxima')
            return redirect(proxima_pagina)
    else:
        flash('usuario nao logado')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
   session['usuario_logado'] = None
   flash('Logout efetuado com susseso!')
   return redirect(url_for('index'))


app.run(debug=True)




