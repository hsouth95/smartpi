import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import time
from daemon import daemon
import requests
import logging

class WeatherBot(daemon):
	
    def run(self):
		logging.basicConfig(filename='/tmp/test.log', level=logging.DEBUG)
		API_ROOT = 'http://api.openweathermap.org/data/2.5/weather'
		config = self.get_config()
		payload = {'q': config['CITY_NAME'], 'APPID': config['API_KEY']}
		while True:
				weather_data = requests.get(API_ROOT,params=payload)
				
				with open(config['FILE_NAME'], 'w') as myfile:
					myfile.write(weather_data.content)
				
				time.sleep(config['TIME_INTERVAL'])

    def get_config(self):
		#need to parse from within this dir
		logging.basicConfig(filename='/tmp/test.log', level=logging.DEBUG)
		try:
			path = os.path.join(sys.path[0], 'weather/config.json')
			logging.info(path)
			with open(path) as config_file:
				return json.load(config_file)
		except:
			logging.error('Unexpected error: ' + sys.exc_info()[0])
			raise


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
		daemon.run()
		sys.exit(0)
