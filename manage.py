# The below is different from the tutorial due to changes in imports
# from Flask - change flask.ext.script or flask.ext.migrate to flask_script
# and flask_migrate respectively
import os
import unittest

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from project import app, db

app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run tests without coverage."""
    tests = unittest.TestLoader().discover('.')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
