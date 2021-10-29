import serial # bibliothèque à installer pyserial : pip install pyserial

ser=serial.Serial('/dev/ttyACM0') #ouvre le port du microbit
ser.baudrate=115200
print(ser)
while True : #on lit en permanence la carte microbit
    if ser.in_waiting :
        texte=ser.read(ser.in_waiting).decode("utf-8")
        print(texte)
