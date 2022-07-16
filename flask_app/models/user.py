from flask_app.config.mysqlconnection import connectToMySQL
import re 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import flash

class User:

    def __init__(self, data):
        self.id = data["id"]
        self.user = data["user"]
        self.career_id = data["career_id"]
        self.collegue_id = data["collegue_id"]
        self.code = data["code"]
        self.num_wp = data["num_wp"]
        self.password = data["password"]
        self.created_at = data["created_at"] 
        self.updated_at = data["updated_at"]
    
    @classmethod
    def save(cls, formulario):
        #formulario = {
        #     "user": "angelaltarodri",
        #     "career": "Derecho",
        #     "code": "20161762",
        #     "num_wp": "944237085",
        #     "password": "91289128snkndsaajdyasdl"
        # }
        query = "INSERT INTO users (user, career_id, collegue_id, code, num_wp, password) VALUES (%(user)s, %(career_id)s, %(collegue_id)s, %(code)s, %(num_wp)s, %(password)s)"
        nuevoId = connectToMySQL('sociedad_de_panes').query_db(query, formulario)
        return nuevoId
    
    @staticmethod
    def valida_usuario(formulario):
        # formulario = {
        #     "user": "angelaltarodri",
        #     "career": "Derecho",
        #     "code": "20161762",
        #     "num_wp": "944237085",
        #     "password": "91289128snkndsaajdyasdl"
        # }

        es_valido = True

        #Validar que mi nombre sea mayor a 2 caracteres
        if len(formulario['user']) < 1:
            flash('El nombre de usuario debe de tener al menos 1 caracter', 'registro')
            es_valido = False
        #Validar que mi apellido sea mayor a 2 caracteres
        if formulario['career_id'] == "0":
            flash('El campo de carrera no debe quedar vacío', 'registro')
            es_valido = False
        if len(formulario['code']) != 8:
            flash('Por favor ingrese su código de alumno correctamente', 'registro')
            es_valido = False
        #Valido email con expresiones regulares #abc123@21msn.com ->NO te aceptaría a.com
        if len(formulario['password']) < 6:
            flash('Contraseña debe tener al menos 8 caracteres', 'registro')
            es_valido = False
        if formulario['password'] != formulario['confirm']:
            flash('Contraseñas no coinciden', 'registro')
            es_valido = False
        
        #Consulta si ya existe ese user
        query = "SELECT id FROM users WHERE user = %(user)s"
        results = connectToMySQL('sociedad_de_panes').query_db(query, formulario)
        if len(results) >= 1:
            flash('Usuario registrado previamente', 'registro')
            es_valido = False

        return es_valido

    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        result = connectToMySQL('sociedad_de_panes').query_db(query, data)
        usr = result[0]
        user = cls(usr)
        return user
    
    @classmethod
    def get_by_user(cls, data):
        # data = {
        #     "email": "cynthia@codingdojo.com",
        #     "password": "1234"
        # }
        query = "SELECT * FROM users WHERE user = %(user)s"
        result = connectToMySQL('sociedad_de_panes').query_db(query, data)
        if len(result) < 1:
            return False
        else :
            usr = result[0]
            #usr = {"id": "1", "first_name": "Elena", "last_name": "De Troya", "email": "elena@cd".......}
            user = cls(usr)
            return user