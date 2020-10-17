import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

RED_PIN = 17
GREEN_PIN = 27
BLUE_PIN = 22

GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)

def blink( red,green,blue ):
    GPIO.output(RED_PIN,red)
    GPIO.output(GREEN_PIN,green)
    GPIO.output(BLUE_PIN,blue)

    time.sleep( 1 )
    GPIO.output(RED_PIN,GPIO.LOW)
    GPIO.output(GREEN_PIN,GPIO.LOW)
    GPIO.output(BLUE_PIN,GPIO.LOW)
    time.sleep( 1 )

blink( GPIO.HIGH, GPIO.LOW, GPIO.LOW )    ## Red
blink( GPIO.HIGH, GPIO.HIGH, GPIO.LOW )   ## Yellow
blink( GPIO.LOW, GPIO.HIGH, GPIO.LOW )    ## Green
blink( GPIO.LOW, GPIO.HIGH, GPIO.HIGH )   ## Cyan
blink( GPIO.LOW, GPIO.LOW, GPIO.HIGH )    ## Blue
blink( GPIO.HIGH, GPIO.LOW, GPIO.HIGH )   ## Magenta
blink( GPIO.HIGH, GPIO.HIGH, GPIO.HIGH )  ## White