from flask import Flask

from .commands import create_tables
from .extensions import login_manager, db

def create_app(config_file="settings.py"):
    app = Flask(__name__)
    
    app.config.from_pyfile(config_file)
    db.init_app(app)
    login_manager.init_app(app)
    
    # login_manager.login_view = ""
    
    # @login_manager.load_user
    # def load_user(id):
    #     User.query.get(id)
    app.cli.add_command(create_tables)
    
    return app