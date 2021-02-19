import microbit as uBit
import time

sensor = DHT11(uBit.pin1)
while True:
    try:
        t , h = sensor.read()
        print("%2.1f%sC  %2.1f%% " % (t, DEGREES, h))
    except DataError as e:
        print("Error : " + str(e))

    time.sleep(2)