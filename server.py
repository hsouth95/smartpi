from flask import Flask, render_template
import json
from modules.connector import Connector


app = Flask(__name__)


@app.route('/')
def hello_world():
	data_engine = Connector()
	return data_engine.get_data()
    
@app.before_first_request
def startup():
	print("hello")
	data_engine = Connector()
	data_engine.start_processes()
