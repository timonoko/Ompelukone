

try:
  import usocket as socket
except:
  import socket

import network,time,machine
from machine import Pin,Timer,ADC

triac=Pin(5, Pin.OUT)  
triac.value(0)

pot = ADC(Pin(15))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

SininenLedi = Pin(2, Pin.OUT)  
SininenLedi.value(0)


goal_speed = 1  # -10 to 10
step_counter = 0

def apply_power(t):
    global step_counter
    if step_counter == 0:
        step_counter = goal_speed
        if step_counter < 0: triac.value(1)
        else: triac.value(0)
    elif step_counter < 0:
        triac.value(0)
        step_counter+=1
    else:
        triac.value(1)
        step_counter-=1

tim = Timer(1)

def set_speed(value):
    global goal_speed,tim
    tim.init(period=11, mode=Timer.PERIODIC, callback=apply_power)
    goal_speed = round(value/5.-10)
    if goal_speed==0: goal_speed=1
    print(f"Motor speed set to: {goal_speed}")

Nollapiste=300

while pot.read()>Nollapiste:
    SininenLedi.value(1)
    time.sleep(0.1)
    SininenLedi.value(0)
    time.sleep(0.1)

SininenLedi.value(0)
    
while True:
  pot_value = pot.read()
  print(pot_value)
  time.sleep(0.1)
  if pot_value<Nollapiste: 
    triac.value(0)
    tim.deinit() # This kills the background timer completely
  else:
    set_speed((pot_value-Nollapiste)/20)
