from time import sleep
import sys
try:
    from mfrc522 import SimpleMFRC522
    import RPi.GPIO as GPIO
except (ImportError, ModuleNotFoundError):
    from dummy_package.mfrc522 import SimpleMFRC522
    import RPiSim.GPIO as GPIO

clreader = SimpleMFRC522()

try:
    while True:
        print("Hold a tag near the reader")
        id, text = reader.read()
        print("ID: %s\nText: %s" % (id,text))
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
