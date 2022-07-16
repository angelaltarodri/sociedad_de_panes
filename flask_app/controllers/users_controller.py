from flask import render_template, redirect, session, request, flash, jsonify
from flask_app import app
from flask_app.models.user import User
from flask_app.models.career import Career
from flask_app.models.post import Post
from flask_app.models.location import Location
import datetime
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index(): 

    careers = Career.get_all()

    return render_template('index.html', careers=careers)

@app.route("/register", methods=['POST'])
def register(): 
    if not User.valida_usuario(request.form):
        return redirect('/')

    pwd = bcrypt.generate_password_hash(request.form['password'])

    formulario = {
        "user": request.form['user'],
        "code": request.form['code'],
        "num_wp": request.form['num_wp'],
        "career_id": request.form['career_id'],
        "collegue_id": request.form['collegue_id'],
        "password": pwd
    }

    id = User.save(formulario)

    session['user_id'] = id

    return redirect('/dashboard')

@app.route("/login", methods=['POST'])
def login():
    user = User.get_by_user(request.form)
    #user = User -> first_name, last_name, password, email ....

    if not user:
        # flash("E-mail no encontrado", "login")
        # return redirect('/')
        return jsonify(message="Usuario no encontrado")
    
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        # flash("Password incorrecto", "login")
        # return redirect('/')
        return jsonify(message="Contraseña incorrecta")
    
    session['user_id'] = user.id
    # return redirect('/dashboard')
    return jsonify(message="Correcto")

@app.route("/dashboard")
def dashboard():
    if 'user_id' not in session:
        return redirect('/')

    data = {
        "id": session['user_id']
    }
    #datos del usuario que ingreso
    user = User.get_by_id(data)
    
    data_admin = {
        "id": "4"
    }
    #todos los posts de data_admin cuyo id es 4 (el id del admin)
    p = Post.get_posts_data_for_page(data_admin)
    #último post
    lp = p[0]

    data_locations = {
        "id": user.collegue_id
    }
    locations = Location.get_all_locations_from_collegue(data_locations)
    #lugares para vender dependiendo del collegue del user
    weekday = datetime.datetime.today().weekday()

    return render_template('dashboard.html', user=user, lp=lp, weekday=weekday, locations=locations)

@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')