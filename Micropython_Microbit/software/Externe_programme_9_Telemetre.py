from microbit import *
from time import sleep_us
from machine import time_pulse_us

def distance(tp, ep):
    tp.write_digital(0)
    sleep_us(2)
    tp.write_digital(1)
    sleep_us(10)
    tp.write_digital(0)
    ep.read_digital()    
    ts = time_pulse_us(ep, 1, 30000)
    if ts > 0: return ts * 17 // 100
    return ts

while True:
    dist = distance(pin0, pin0) #carte Grove Trigger et Echo sur la même broche
    print(dist) #en mm
    sleep(500)