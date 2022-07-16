from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Reaction_has_comment:
    def __init__(self, data):
        self.reaction_id = data ["reaction_id"]
        self.comment_id = data ["comment_id"]
        self.user_id = data ["user_id"]
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO reactions_has_comments(reaction_id, comment_id, user_id) VALUES (%(reaction_id)s, %(comment_id)s, %(user_id)s);" 
        nuevoId = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return nuevoId
    @classmethod
    def get_reactions_by_post(cls, data):
        query = "SELECT * FROM reactions_has_comments LEFT JOIN comments ON comments.post_id WHERE reactions_has_comments.comment_id = comments.id AND comments.post_id = %(post_id)s;" 
        nuevoId = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return nuevoId
    @classmethod
    def quit(cls, data):
        query = "DELETE FROM reactions_has_comments WHERE (comment_id = %(comment_id)s) and (user_id = %(user_id)s) and (reaction_id = %(reaction_id)s);" 
        nuevoId = connectToMySQL("sociedad_de_panes").query_db(query, data)
        return nuevoId