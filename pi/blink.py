import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RED_PIN = 17

GPIO.setup(RED_PIN, GPIO.OUT)

while True:
    GPIO.output(RED_PIN,GPIO.HIGH)
    time.sleep( 1 )
    GPIO.output(RED_PIN,GPIO.LOW)
    time.sleep( 1 )