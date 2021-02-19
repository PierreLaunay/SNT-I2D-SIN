b=BME280()
while 1:
    sleep(500)
    print(b.get())