
import os
import gc
import time
import machine
from machine import Pin, ADC, PWM
import neopixel
import random

battery = ADC(34)          # Battery sensor
ldrsens = Pin(35, Pin.IN)  # LDR (light) sensor (GL5516)
matrix  = Pin(32, Pin.OUT) # Matrix
lbutton = Pin(26, Pin.IN, Pin.PULL_UP) # Left button
mbutton = Pin(27, Pin.IN, Pin.PULL_UP) # Middle button
rbutton = Pin(14, Pin.IN, Pin.PULL_UP) # Right button
buzzer  = Pin(15, Pin.OUT) # Buzzer
sht3x_1 = Pin(21, Pin.IN)  # Temperature and Humidity Sensors (SHT3x)
sht3x_2 = Pin(22, Pin.IN)

print('{0} MHz clock frequeny'.format(machine.freq()/1000000))
print('{0} kB free RAM'.format(gc.mem_free()/1024))
s = os.statvfs('//')
print('{0} MB free flash memory'.format((s[0]*s[3])/1048576))

print("Battery", battery.read(), "Left", lbutton.value(), "Mid", mbutton.value(), "Right", rbutton.value())

def sound_buzzer():
    tone = PWM(buzzer, freq=2000, duty_u16=32637)
    time.sleep(1)
    tone.deinit()

def np_black(np):
    for i in range(256):
        np[i] = (0, 0, 0)
    np.write()

def rnd():
    return random.randint(0, 128)

def np_random1(np):
    for i in range(256):
        np[i] = (rnd(), rnd(), rnd())
    np.write()

def np_random2(np):
    np[random.randint(0, 255)] = (rnd(), rnd(), rnd())
    np.write()
    
sound_buzzer()
np = neopixel.NeoPixel(matrix, 256)
np_black(np)
for i in range(100):
    np_random1(np)
np_black(np)
for i in range(800):
    np_random2(np)
np_black(np)
