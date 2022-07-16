from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Reaction_has_post:
    def __init__(self, data):
        self.reaction_id = data ["reaction_id"]
        self.post_id = data ["post_id"]
        self.user_id = data ["user_id"]
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO reactions_has_posts(reaction_id, post_id, user_id) VALUES (%(reaction_id)s, %(post_id)s, %(user_id)s);" 
        nuevoId = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return nuevoId
    @classmethod
    def get_reactions_by_post(cls, data):
        query = "SELECT * FROM reactions_has_posts WHERE post_id = %(post_id)s;" 
        nuevoId = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return nuevoId
    @classmethod
    def quit(cls, data):
        query = "DELETE FROM reactions_has_posts WHERE (post_id = %(post_id)s) and (user_id = %(user_id)s) and (reaction_id = %(reaction_id)s);" 
        nuevoId = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return nuevoId