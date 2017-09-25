"""Create an application instance."""
from flask.helpers import get_debug_flag

from cat_dog.app import create_app
from cat_dog.settings import DevelopmentConfig, ProductionConfig

application = create_app(DevelopmentConfig if get_debug_flag() else ProductionConfig)
