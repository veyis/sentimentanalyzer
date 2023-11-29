# -*- encoding: utf-8 -*-
"""
Refactored code for better practices and security
"""
from apps.home import blueprint

from flask import Flask, render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound
from pymongo import MongoClient
import os

# Initialize Flask application
app = Flask(__name__)

# Blueprint setup if needed (assuming blueprint is correctly set up elsewhere)
# from apps.home import blueprint
# app.register_blueprint(blueprint)

# # MongoDB connection setup
# try:

#     # MongoDB connection setup
#     MONGO_DB_URI = os.environ.get('MONGO_DB_URI')  # Set this in your environment variables
#     DB_NAME = "stock_comments"
#     COLLECTION_NAME = "news_ticker_sentiments"

#     # MongoDB client initialization
#     mongo_client = MongoClient(MONGO_DB_URI)
#     db = mongo_client[DB_NAME]
#     collection = db[COLLECTION_NAME]

#     data=collection.find_one()

# except Exception as e:
#     print("Error connecting to MongoDB: %s" % e)

@blueprint.route('/index')

@login_required
def index():
    try:
        #data = collection.find_one()
        return render_template('home/index.html', segment='index', data={"name":"sai"})
    except Exception as e:
        print(f"Error fetching data from MongoDB: {e}")
        return render_template('home/page-500.html'), 500

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
