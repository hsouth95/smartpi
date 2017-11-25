import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import time
from daemon import daemon
import requests

class WeatherBot(daemon):
    def run(self):
		API_ROOT = 'http://api.openweathermap.org/data/2.5/weather'
		config = self.get_config()
		
		payload = {'q': config['CITY_NAME'], 'APPID': config['API_KEY']}
		while True:
				weather_data = requests.get(API_ROOT,params=payload)
				
				with open(config['FILE_NAME'], 'w') as myfile:
					myfile.write(weather_data.content)
				
				time.sleep(config['TIME_INTERVAL'])

    def get_config(self):
		with open('config.json') as config_file:
			return json.load(config_file)


if __name__ == '__main__':
	daemon = WeatherBot('/tmp/weather.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			sys.exit(2)
	else:
		print("usage: %s start|stop|restart" % sys.argv[0])
		sys.exit(0)
