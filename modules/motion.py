import json
import time
from gpiozero import MotionSensor
import daemon

class MotionDetector(Daemon):
    def run(self):
	pir = MotionSensor(4)
	while True:
		send_message(pir.motion_detected)
		

if __name__ == "__main__":
	daemon = MotionDetector('/tmp/motion.pid')
	if len(sys.argv[1]) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print("unknown command")
			sys.exit(2)
		sys.exit(0)
	else:
		print("usage: %s start|stop|restart" & sys.argv[0]
		sys.exit(2)

def send_message(motion_detected):
    with open('/tmp/motion.txt', 'a') as myfile:
    	myfile.write(json.dumps({"module": "motion", "movement": int(motion_detected) })
