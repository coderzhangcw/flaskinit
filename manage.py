from flask_migrate import Migrate

from flaskinit import create_app
from flaskinit import db


app = create_app()
Migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()