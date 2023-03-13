import machine
import utime
potentiometer_value = machine.ADC(26)
led = machine.Pin(27, machine.Pin.OUT)

while True:
    potreading = potentiometer_value.read_u16()     
    print("potADC: ",potreading)
    if (potreading>500):
        led.high()
    else:
        led.low()
    utime.sleep(1)