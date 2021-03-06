from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, UserMixin
from flask_migrate import Migrate
from flask.logging import default_handler
from logging.handlers import RotatingFileHandler
import logging
import os

##### Flask Extensions #####
db = SQLAlchemy()
db_migration = Migrate()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'




##### Application Factory Function #####

def create_app():
    app = Flask(__name__)

    #configure flask app
    config_type = os.getenv('CONFIG_TYPE', default='config.DevelopmentConfig')
    app.config.from_object(config_type)

    #configure logging
    configure_logging(app)

    #register blueprints
    register_blueprints(app)

    #register callbacks
    register_callbacks(app)

    #initialize flask extensions
    initialize_extensions(app)

    #register error handlers
    register_error_handlers(app)

    return app

##### Helper Functions #####

def configure_logging(app):
    file_handler = RotatingFileHandler('instance/task-master.log', maxBytes= 16384, backupCount=20)
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(filename)s: %(lineno)d]')
    file_handler.setFormatter(file_formatter)
    app.logger.addHandler(file_handler)
    app.logger.removeHandler(default_handler)

def register_blueprints(app):
    from project.auth import auth_blueprint
    from project.main import main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

def register_callbacks(app):
    pass

def initialize_extensions(app):
    db.init_app(app)
    db_migration.init_app(app, db)
    bootstrap.init_app(app)
    login_manager.init_app(app)

def register_error_handlers(app):
    @app.errorhandler(403)
    def forbidden_error(error):
        return render_template('403.html'), 403

    @app.errorhandler(404)
    def not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return render_template('405.html'), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('500.html'), 500





