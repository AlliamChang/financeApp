import app
from flask_script import Manager


manager = Manager(app.create_app('runing'))
manager.run()

