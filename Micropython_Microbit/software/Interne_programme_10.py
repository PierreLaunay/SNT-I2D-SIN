from microbit import *
while True :
  geste = accelerometer.current_gesture()
  print(geste)
  sleep(200)