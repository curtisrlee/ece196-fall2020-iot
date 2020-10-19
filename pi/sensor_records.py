import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import adafruit_dht
import board
import time

# Setup DHT Sensor.
# Can change pin or DHT type if needed.
dht_sensor = adafruit_dht.DHT22(board.D4)

# Setup Firebase, replace with your info.
cred = credentials.Certificate( 'PATH_TO_FIREBASE_KEY' )
firebase_admin.initialize_app( cred, { 'databaseURL':  'LINK_TO_DATABASE_URL' } )

while True:
    try:
        # Read the data
        temp = dht_sensor.temperature
        hum = dht_sensor.humidity
    except RuntimeError as error: 
        # Handle routine errors.
        # The sensor is pretty derpy and often doesn't output properly.
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        # Handle other errors.
        dht_sensor.exit()
        raise error

    # print to console
    print("Temperature =", temp, 'C')
    print("Humidity =", hum, '%')

    # Sync data to Firebase
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

    # run every 5 seconds
    time.sleep( 5 )