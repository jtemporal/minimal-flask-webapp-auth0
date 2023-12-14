from flask import Flask

from config import config
from webapp.views import webapp_bp


app = Flask(__name__)
app.secret_key = config["WEBAPP"]["SECRET_KEY"]

app.register_blueprint(webapp_bp, url_prefix='/')
