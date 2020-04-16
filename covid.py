## covid.py
from flask import Flask

app = Flask(__name__, root_path='app/')
from app import routes
