import os

class Config:
    """Base configuration class."""
    DEBUG = True
    PORT = 5000
    HOST = '0.0.0.0'
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-secret-key')
    
class DevelopmentConfig(Config):
    """Development configuration."""
    ENV = 'development'

class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False
    ENV = 'production'

# Dictionary to map environment names to config classes
config_dict = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
