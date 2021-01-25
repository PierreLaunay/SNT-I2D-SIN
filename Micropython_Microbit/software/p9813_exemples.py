from microbit import pin0,pin14
import p9813
pin0.write_digital(0)
pin14.write_digital(0)
chain = p9813.P9813(pin0,pin14,2,1)
chain[0] = (255, 0, 0)
chain[1] = (0, 255, 0)
chain.write()