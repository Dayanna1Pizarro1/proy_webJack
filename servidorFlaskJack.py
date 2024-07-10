Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask, render_template, request, redirect, url_for, flash
... 
... app = Flask(proy)
... app.secret_key = 'superkey123'

... # Usuarios válidos 
valid_users = ['admin', 'UsuariotipoA', 'Usuariotipob']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    username = request.form['username']
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Validar usuario
    if username not in valid_users:
        flash('Usuario no válido. Por favor, inténtalo de nuevo.')
        return redirect(url_for('home'))
    
    # Lógica para manejar el mensaje, como enviarlo por correo electrónico.
    return f"Mensaje enviado por {name} ({email}): {message}"

if proy == 'main':
    app.run(debug=True)

