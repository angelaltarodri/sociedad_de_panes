from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Location:
    def __init__(self, data):
        self.id = data ["id"]
        self.day = data ["day"]
        self.location = data ["location"]
        self.reference = data ["reference"]
        self.created_at = data ["created_at"]
        self.updated_at = data ["updated_at"]
        self.collegue_id = data ["collegue_id"]
    @classmethod
    def get_all_locations_from_collegue(cls, data):
        query = "SELECT * FROM locations LEFT JOIN collegues ON collegues.id WHERE locations.collegue_id = collegues.id AND collegues.id = %(id)s;"
        results = connectToMySQL("sociedad_de_panes").query_db(query, data)
        locations = []
        for loc in results:
            rec = cls(loc)
            locations.append(rec)
        return locations