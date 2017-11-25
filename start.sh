#!/bin/bash
python modules/weather/weather.py start
export FLASK_APP=server.py
flask run
