from time import sleep
import sys
try:
    from mfrc522 import SimpleMFRC522
    import RPi.GPIO as GPIO
except ImportError:
    from dummy_package.mfrc522 import SimpleMFRC522
    import RPiSim.GPIO as GPIO

reader = SimpleMFRC522()

try:
    while True:
        print("Hold a tag near the reader")
        tes = reader.read()
#         print("ID: %s\nText: %s" % (id,text))
        print(tes)
        sleep(5)
except KeyboardInterrupt:
    GPIO.cleanup()
    raise
