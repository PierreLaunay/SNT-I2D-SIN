# http://www.multiwingspan.co.uk/micro.php?page=rtc
from microbit import *

def bcd2dec(bcd):
    return (((bcd & 0xf0) >> 4) * 10 + (bcd & 0x0f))

def dec2bcd(dec):
    tens, units = divmod(dec, 10)
    return (tens << 4) + units
    
def get_time():
    i2c.write(addr, b'\x00', repeat=False)
    buf = i2c.read(addr, 7, repeat=False)
    bufs[0] = bcd2dec(buf[0])
    bufs[1] = bcd2dec(buf[1])
    if buf[2] & 0x40:
        hh = bcd2dec(buf[2] & 0x1f)
        if buf[2] & 0x20:
            hh += 12
    else:
        hh = bcd2dec(buf[2])
    bufs[2]=hh
    bufs[3] = buf[3]
    bufs[4] = bcd2dec(buf[4])
    bufs[5] = bcd2dec(buf[5] & 0x1f)
    bufs[6] = bcd2dec(buf[6])
    #print(wday,DD,MM,YY,hh,mm,ss)
    return bufs
    
def set_time(s,m,h,w,dd,mm,yy):
    t = bytes([s,m,h,w,dd,mm,yy-2000])
    for i in range(0,7):
        i2c.write(addr, bytes([i,dec2bcd(t[i])]), repeat=False)
    return

addr = 0x68
buf = bytearray(7)
bufs = bytearray(7)
set_time(15,03,22,3,23,12,2020)
sleep(1000)

def affichage_temps() :
    temps=get_time()
    heure=' '+str(temps[2])+":"+str(temps[1])+":"+str(temps[0])
    jour=str(temps[4])+"/"+str(temps[5])+"/"+str(2000+temps[6])
    uart.write(jour)
    uart.write(heure)
    uart.write('\n')

if __name__ == '__main__':
    affichage_temps() 
