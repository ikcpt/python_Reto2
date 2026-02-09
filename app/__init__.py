from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager   

db = SQLAlchemy()
login_manager = LoginManager()        

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///python.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 
    app.config["SECRET_KEY"] = "dev-secret-key"

    db.init_app(app)
    login_manager.init_app(app)       
    login_manager.login_view = 'auth.login' 

    from app.models.usuario import Usuario
    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.query.get(int(user_id))
    
    from app.controllers.navigation_controller import navigation_bp
    app.register_blueprint(navigation_bp)
    
    from app.controllers.libros_controller import libros_bp
    app.register_blueprint(libros_bp)
    
    from app.controllers.api_controller import api_bp
    app.register_blueprint(api_bp)
    
    from app.controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp)

    from app.controllers.socios_controller import socios_bp
    app.register_blueprint(socios_bp)
    
    from app.api.routes import api_bp
    app.register_blueprint(api_bp)

    with app.app_context():
        db.create_all()

    return app