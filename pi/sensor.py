import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
    hum, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    print("Temperature =", temp)
    print("Humidity =", hum)
    time.sleep( 2 )