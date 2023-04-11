# app.py
import config
import os
from flask import Flask, jsonify
# from flask_sqlalchemy import SQLAlchemy
from model import db
from flask_cors import CORS
from flask.blueprints import Blueprint
from flask_restful import Api

# Initialize Flask APP
app = Flask(__name__)
app.url_map.strict_slashes = False

# Set CORS header
cors = CORS(app)

# Load the appropriate environment configuration based on the 'env' environment variable
try:
    if os.environ.get('env') == 'PROD':
        app.config.from_object(config.ProdConfig)
    elif os.environ.get('env') == 'DEV':
        app.config.from_object(config.DevConfig)
    else:
        app.config.from_object(config.LocalConfig)
except Exception as e:
    print(f"Error loading environment configuration: {e}")


# db = SQLAlchemy(app)
db.init_app(app)

# Define a custom error handler for 404 (Not Found) errors
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

class Routes:
    def __init__(self) -> None:
        pass
    
    # Load API routes from the 'route' module
    def load_api():
        from route import typeahead
        from route import search
        from route import export
        api.add_resource(typeahead.TypeAheadResult, '/typeahead')
        api.add_resource(search.SearchResult, '/search/<profile_id>')
        api.add_resource(export.ExportResult, '/export/<profile_id>')

# Load API routes and register the blueprint with the Flask app
Routes.load_api()
app.register_blueprint(api_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
