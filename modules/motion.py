import json
import time
from gpiozero import MotionSensor

pir = MotionSensor(4)
while True:
    send_message(pir.motion_detected)
    time.sleep(5)



def send_message(motion_detected):
    print json.dumps({"module": "motion", "movement": int(motion_detected) })
