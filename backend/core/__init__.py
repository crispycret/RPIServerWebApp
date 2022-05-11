from datetime import datetime, timedelta

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from sqlalchemy.orm import backref
from sqlalchemy import MetaData


from config import Configuration



api = Flask(__name__)
api.config.from_object(Configuration)


# Authentication headers will be required when enabled
# CORS(api)


db = SQLAlchemy(api)

api.config['JWT_SECRET_KEY'] = 'secret-key place holder'
api.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1)


# Used for migrating tables (not used)
naming_convention = {
    'ix': 'ix_$(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(column_0_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s'
}

# Set database metadata using the above naming conventions.
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))

# Perform database migrations.
migrate = Migrate(api, db, render_as_batch=True)


login = LoginManager(api)

# auth not used
# Register modulerized task such as authentication and collections (plant data)
from .auth import auth as auth_blueprint
api.register_blueprint(auth_blueprint)

from .collection import collection as collection_blueprint
api.register_blueprint(collection_blueprint)


# Import request handlers
from core import views



# live_tracker.py
## Live Tracker of the plant data api
## Time based event -> periodic event


from apscheduler.schedulers.background import BackgroundScheduler


from core.periodic_events import fetch_live_data


# Schedule a job to be executed every minute.
# The job is to grab live plant api data and save it to the database. 
scheduler = BackgroundScheduler()


# job = scheduler.add_job(fetch_data, 'interval', minutes=1)
job = scheduler.add_job(fetch_live_data, 'interval', minutes=1)



# Start the scheduler
scheduler.start()





