from microbit import *
from lcd_i2c import LCD1602

lcd = LCD1602()

while True:
  lcd.setCursor(0,0)
  lcd.writeTxt(str(temperature()))