import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def cb(*args):
    print("Button was pushed!")

GPIO.add_event_detect(10, edge=GPIO.FALLING, callback=cb, bouncetime=200)

input("press enter 2 quit\n")