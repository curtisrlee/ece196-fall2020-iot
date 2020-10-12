import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
# import Adafruit_DHT

import random
import datetime as dt

# DHT_SENSOR = Adaruit_DHT.DHT22
DHT_PIN = 4

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app( cred, { "databaseURL": "https://ece196-fall2020-curtis-dev.firebaseio.com/" } )

while True:
    # hum, temp = Adaruit_DHT.read_retry(  DHT_SENSOR,  DHT_PIN  )
    hum = random.randrange(10, 90)
    temp = random.randrange(10, 40)

    temp_ref = db.reference( "data/sensor/temperature" )
    temp_ref.set( temp )

    hum_ref = db.reference( "data/sensor/humidity" )
    hum_ref.set( hum )

    records_ref = db.reference( "data/records" )
    records_ref.push({
      'timestamp': {'.sv': 'timestamp'},
      'temperature': temp,
      'humidity': hum,
    })

    print( "Humidity =", hum )
    print( "Temperature =", temp)

    time.sleep( 2 )