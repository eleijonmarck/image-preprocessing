"""Test configs."""
from cat_dog.app import create_app
from cat_dog.settings import DevelopmentConfig, ProductionConfig

def test_production_config():
    """Production config."""
    app = create_app(ProductionConfig)
    assert app.config['ENV'] == 'production'
    assert app.config['DEBUG'] is False


def test_dev_config():
    """Development config."""
    app = create_app(DevelopmentConfig)
    assert app.config['ENV'] == 'development'
    assert app.config['DEBUG'] is True
