from microbit import *
from machine import time_pulse_us
import utime
start = utime.ticks_ms()
from lcd_i2c import LCD1602

lcd = LCD1602()

def getUltrasonicData(trig, echo, data='distance', timeout_us=30000):
    trig.write_digital(0)
    utime.sleep_us(2) # Delay for given number of microseconds, should be positive or 0.
    trig.write_digital(1)
    utime.sleep_us(10) # https://github.com/bbcmicrobit/micropython/blob/master/docs/utime.rst
    trig.write_digital(0)
    echo.read_digital()
    duration = time_pulse_us(echo, 1, timeout_us)
    if data=='distance': return 17*duration/1000       #340*duration/2e4
    elif data == 'duration': return duration

while True:
    if utime.ticks_diff(utime.ticks_ms(),start) > 100 : #raffraichissement tous les 100 ms
        lcd.setCursor(0,0)
        lcd.writeTxt(str(getUltrasonicData(pin0, pin0, 'distance')) + ' cm  ')
        start = utime.ticks_ms()

""" method:: machine.time_pulse_us(pin, pulse_level, timeout_us=1000000)
    Time a pulse on the given *pin*, and return the duration of the pulse in
    microseconds. The *pulse_level* argument should be 0 to time a low pulse or
    1 to time a high pulse."""
#https://github.com/bbcmicrobit/micropython/blob/master/source/extmod/machine_pulse.c