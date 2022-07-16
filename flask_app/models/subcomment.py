from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Subcomment:
    def __init__(self, data):
        self.id = data ["id"]
        self.content = data ["content"]
        self.comment_id = data["comment_id"]    
        self.post_id = data["post_id"]    
        self.user_id = data["user_id"]    
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    @staticmethod
    def valida_subcomentario(formulario): 
        es_valido = True

        if len(formulario['content']) < 1 :
            flash('El contenido debe tener al menos 1 caracter', 'comentario')
            es_valido = False

        if len(formulario['content']) > 200 :
            flash('El contenido debe tener máximo 200 caracteres', 'comentario')
            es_valido = False
        
        return es_valido
    @classmethod
    def save(cls, data):
        query = "INSERT INTO subcomments (content, user_id, comment_id) VALUES (%(content)s, %(user_id)s, %(comment_id)s);" 
        nuevoId = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return nuevoId

    @staticmethod
    def get_date_object(date):
        date_object = {
            "year" : str(date['updated_at'])[0:4],
            "month" : str(date['updated_at'])[5:7],
            "day" : str(date['updated_at'])[8:10],
            "hour" : str(date['updated_at'])[11:13],
            "minute" : str(date['updated_at'])[14:16],
            "second" : str(date['updated_at'])[17:19],
        }
        return date_object
    @staticmethod
    def get_all_subcomments_by_post_id(data):
        query = "SELECT subcomments.id as subcomment_id, subcomments.content as contenido,  subcomments.updated_at as updated_at, subcomments.user_id as usuario, comments.id as comment_id, comments.post_id as publicacion_usuario, users.user as user_name FROM subcomments LEFT JOIN users ON users.id LEFT JOIN comments ON comments.id LEFT JOIN posts ON posts.id WHERE subcomments.comment_id = comments.id AND comments.post_id = posts.id AND posts.id = %(post_id)s AND users.id = subcomments.user_id ORDER BY subcomments.updated_at ASC;"
        results = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return results

    @classmethod
    def get_subcomments_data_for_page(cls, data):
        results = cls.get_all_subcomments_by_post_id(data)
        subcomments = []
        for subcomentario in results:
            subcomment = {
                "id" : subcomentario["subcomment_id"],
                "content" : subcomentario["contenido"],
                "updated_at" : subcomentario["updated_at"],
                "user_id" : subcomentario["usuario"],
                "post_id" : subcomentario["publicacion_usuario"],
                "comment_id" : subcomentario["comment_id"],
                "user_name" : subcomentario["user_name"],
                "updated_at_object" : cls.get_date_object(subcomentario),
            }

            subcomment["hour_int"] = int(subcomment["updated_at_object"]["hour"])
            
            subcomments.append(subcomment)
        return subcomments

    @staticmethod
    def delete_subcomment_by_subcomment_id(data):
        query = "DELETE FROM subcomments WHERE (id = %(id)s);"
        result = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return result

    @staticmethod
    def delete_subcomments_by_comment_id(data):
        query = "DELETE FROM subcomments WHERE comment_id = %(comment_id)s;"
        result = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return result