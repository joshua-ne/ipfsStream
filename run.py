import os
from app import create_app




if __name__ == '__main__':
    config_name = os.getenv('FLASK_CONFIG')
    config_name = 'production'
    app = create_app(config_name)
    app.run()
