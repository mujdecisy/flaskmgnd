import yaml

from flaskmgnd.daflask import DaFlask
from flaskmgnd.util.damongo import DaMongo
from flaskmgnd.util.log import configure_logger
from flaskmgnd.util.blueprint import util_blueprints
from flaskmgnd.mvc.controllers import controller_blueprints

def create_app(test_config=None):
    app = DaFlask(__name__, instance_relative_config=True)
    
    load_config(app, test_config)
    configure_logger(app)
    connect_mongo(app)

    app.register_blueprint(util_blueprints)
    app.register_blueprint(controller_blueprints)
    
    return app


def load_config(app, test_config):
    if test_config is None:
        app.config.from_file('config.yml', load=yaml.safe_load)
    else:
        app.config.from_mapping(test_config)


def connect_mongo(app):
    app.mng = DaMongo(app.config["MONGO"])