from flask_app import app

#Importación de controladores
from flask_app.controllers import users_controller
from flask_app.controllers import posts_controller
from flask_app.controllers import comments_controller
from flask_app.controllers import subcomments_controller
from flask_app.controllers import reactions_controller

if __name__ == "__main__":
    app.run(debug=True)