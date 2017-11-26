import subprocess
import json

CONFIG_FILE = "modules/modules.json"


class Connector():
	def get_data(self):
		json_data = None
		with open(CONFIG_FILE, 'r') as json_file:
			json_data = json.load(json_file)

		data = []
		for module in json_data:
			with open(module['file_name']) as f:
				data.append(
					{'name': module['name'],
					 'data': json.load(f)
					})

		return json.dumps(data)
	
	def start_processes(self):
		json_data = None
		with open(CONFIG_FILE, 'r') as json_file:
			json_data = json.load(json_file)
			print(json_data)

		for module in json_data:
			subprocess.call(str(module['start_command']), shell=True)
		
