from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Comment:
    def __init__(self, data):
        self.id = data ["id"]
        self.content = data ["content"]
        self.post_id = data["post_id"]    
        self.user_id = data["user_id"]    
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    @staticmethod
    def valida_comentario(formulario): 
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
        query = "INSERT INTO comments (content, user_id, post_id) VALUES (%(content)s, %(user_id)s, %(post_id)s);" 
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
    def get_all_comments_by_post_id(data):
        query = "SELECT comments.id as comment_id, comments.content as contenido, comments.updated_at , comments.user_id as comentario_usuario, posts.user_id as publicacion_usuario, users.user as user_name FROM comments LEFT JOIN posts ON posts.id LEFT JOIN users ON users.id WHERE posts.id = post_id AND users.id = comments.user_id AND post_id = %(post_id)s ORDER by updated_at ASC;"
        results = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return results

    @classmethod
    def get_comments_data_for_page(cls, data):
        results = cls.get_all_comments_by_post_id(data)
        comments = []
        for comentario in results:
            comment = {
                "id" : comentario["comment_id"],
                "content" : comentario["contenido"],
                "updated_at" : comentario["updated_at"],
                "user_id" : comentario["comentario_usuario"],
                "post_id" : comentario["publicacion_usuario"],
                "user_name" : comentario["user_name"],
                "updated_at_object" : cls.get_date_object(comentario),
            }

            comment["hour_int"] = int(comment["updated_at_object"]["hour"])
            
            comments.append(comment)
        return comments
    @staticmethod
    def delete_comment_by_comment_id(data):
        query = "DELETE FROM comments WHERE (id = %(id)s);"
        result = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return result

    @staticmethod
    def delete_comments_by_post_id(data):
        query = "DELETE FROM comments WHERE post_id = %(post_id)s;"
        result = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return result