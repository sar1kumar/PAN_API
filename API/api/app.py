from flask import Flask
from flask_restx import Api
import os
from flask_mongoengine import MongoEngine
from flask_jwt_extended import JWTManager
from routes import create_routes

database_name = "pan_data"
DB_URI = "mongodb+srv://<name>:<password>@<dbname>.9h5jq.mongodb.net/pan_data?retryWrites=true&w=majority"

# Change the above URI to your DB Uri from mongo cloud using connect option.


app = Flask(__name__)

api = Api(app, version='1.0', title='PAN DATA API', description='A simple PAN data retrieval API')
app.config["MONGODB_HOST"] = DB_URI


app.config['JWT_SECRET_KEY'] = "{Seceret Key}" # Set your own secret key in place of {Secret Key}

    # init api and routes

create_routes(api=api)

# init mongoengine
db = MongoEngine(app=app)

# init jwt manager
jwt = JWTManager(app=app)

if __name__ == '__main__':
    # Main entry point when run in stand-alone mode.
    app.run(debug=True)
