import machine 
import utime 
buzzer = machine.Pin(15, machine.Pin.OUT) 
while True:
    for i in range(80):
       buzzer.value(1)
       utime.sleep(0.001)
       buzzer.value(0)
       utime.sleep(0.001)

    for i in range(100):
       buzzer.value(1)
       utime.sleep(0.002)
       buzzer.value(0)
       utime.sleep(0.002)
