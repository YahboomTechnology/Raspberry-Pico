import machine 
import utime

led = machine.PWM(machine.Pin(15))
led.freq(1000)

while True:
    for i in range(65535):
        led.duty_u16(i)
        utime.sleep(0.0005)