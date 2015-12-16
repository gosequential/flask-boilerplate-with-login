#!/usr/bin/env python
import os
from flask.ext.script import Manager, Shell, Server
from app import create_app, db
from app.models import BetaRequest, CurrentWeather


app = create_app(os.getenv('FLASK_CONFIG') or 'default') 
manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db, BetaRequest=BetaRequest, CurrentWeather=CurrentWeather)

manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("runserver", Server(host="0.0.0.0", port=5001, threaded=True))


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__': 
    manager.run()
