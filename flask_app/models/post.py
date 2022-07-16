from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Post:
    def __init__(self, data):
        self.id = data ["id"]
        self.title = data ["title"]
        self.content = data ["content"]
        self.user_id = data["user_id"]    
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    @staticmethod
    def valida_publicacion(formulario): 
        es_valido = True

        if len(formulario['title']) < 3 :
            flash('El nombre de la publicación debe tener al menos 3 caracteres', 'publicacion')
            es_valido = False
            
        if len(formulario['title']) > 50 :
            flash('El nombre de la publicación debe tener menos de 50 caracteres', 'publicacion')
            es_valido = False

        if len(formulario['content']) < 4 :
            flash('El contenido debe tener al menos 4 caracteres', 'publicacion')
            es_valido = False

        if len(formulario['content']) > 100 :
            flash('El contenido debe tener máximo 100 caracteres', 'publicacion')
            es_valido = False
        
        return es_valido
    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts(title, content, user_id) VALUES ( %(title)s, %(content)s, %(user_id)s);" 
        nuevoId = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return nuevoId
    
    @classmethod
    def assign_category_to_post(cls, data):
        query = "SELECT posts.id as id_publicacion from users LEFT JOIN posts ON posts.user_id WHERE users.id = posts.user_id AND users.id = %(id)s ORDER by id_publicacion ASC;"
        results = connectToMySQL("sociedad_de_panes").query_db(query, data)
        last_result = results[len(results) - 1]

        data['post_id'] = last_result['id_publicacion']

        query = "INSERT INTO postcategories_has_posts(postcategory_id, post_id) VALUES (%(category_id)s , %(post_id)s);"
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
    @classmethod
    def get_all_posts(cls, data):
        query = "SELECT posts.id, posts.title, posts.content, posts.updated_at, posts.user_id from users LEFT JOIN posts ON posts.user_id WHERE users.id = posts.user_id AND users.id = %(id)s ORDER BY updated_at DESC;"
        results = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return results

    @staticmethod
    def get_all_comments_by_post_id(data):
        query = "SELECT * FROM comments LEFT JOIN posts ON posts.id LEFT JOIN users ON users.id WHERE posts.id = post_id AND users.id = comments.user_id AND post_id = %(id)s;"
        results = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return results

    @classmethod
    def get_posts_data_for_page(cls, data):
        results = cls.get_all_posts(data)
        posts = []
        for publicacion in results:

            post = {
                "id" : publicacion["id"],
                "title" : publicacion["title"],
                "content" : publicacion["content"],
                "updated_at" : publicacion["updated_at"],
                "user_id" : publicacion["user_id"],
                "updated_at_object" : cls.get_date_object(publicacion),
            }

            post["hour_int"] = int(post["updated_at_object"]["hour"])

            post["cant_comments"] = len(cls.get_all_comments_by_post_id(post))
            
            posts.append(post)
        return posts

    @classmethod
    def get_post_data_for_page(cls, data):
        query = "SELECT * FROM posts WHERE id = %(post_id)s;"
        result = connectToMySQL("sociedad_de_panes").query_db(query, data)
        post = result[0]
        
        publicacion = {
            "id" : post["id"],
            "title" : post["title"],
            "content" : post["content"],
            "updated_at" : post["updated_at"],
            "user_id" : post["user_id"],
            "updated_at_object" : cls.get_date_object(post),
        }

        publicacion["hour_int"] = int(publicacion["updated_at_object"]["hour"])
        return publicacion
    
    @staticmethod
    def delete_post(data):
        query = "DELETE FROM posts WHERE id = %(post_id)s"
        result = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return result

    @staticmethod
    def delete_post_from_categories(data):
        query = "DELETE FROM postcategories_has_posts WHERE post_id = %(post_id)s;"
        result = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return result