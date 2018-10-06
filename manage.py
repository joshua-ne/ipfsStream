from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import db, create_app
import os

config_name = os.getenv('FLASK_CONFIG')
config_name = 'production'
app = create_app(config_name)

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


if __name__ == "__main__":
    manager.run()