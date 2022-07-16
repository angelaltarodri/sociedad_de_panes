from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Career:
    def __init__(self, data):
        self.id = data ["id"]
        self.name = data ["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM careers" 
        results = connectToMySQL("sociedad_de_panes").query_db(query)
        carreras = []
        for carrera in results:
            car = cls(carrera)
            carreras.append(car)
        return carreras
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM careers WHERE id = %(id)s"
        result = connectToMySQL("sociedad_de_panes").query_db(query, data)
        carrera = cls(result[0])
        return carrera
    