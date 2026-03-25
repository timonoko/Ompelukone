
print('Testing 5')

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
    tim.init(period=20, mode=Timer.PERIODIC, callback=apply_power)
    goal_speed = round(value/5.-10)
    if goal_speed==0: goal_speed=1
    print(f"Motor speed set to: {goal_speed}")
    
while pot.read()>500:
    SininenLedi.value(1)
    time.sleep(0.1)
    SininenLedi.value(0)
    time.sleep(0.1)

SininenLedi.value(0)
    
while True:
  pot_value = pot.read()
  print(pot_value)
  time.sleep(0.1)
  if pot_value<500: 
    triac.value(0)
    tim.deinit() # This kills the background timer completely
  else:
    set_speed((pot_value-500)/25)

"""
while True:
    s.settimeout(0.2)
    try:
        conn, addr = s.accept()
        request = conn.recv(1024)
        request = str(request)
        s.settimeout(5.0)
        if request.find('/ON') == 6:
            tim.deinit() # This kills the background timer completely
            relayState=1
            triac.value(1)
        if request.find('/OFF') == 6:
            relayState=0
            triac.value(0)
            tim.deinit() # This kills the background timer completely
            print("Motor Hard Stopped and Timer Deactivated")
        if request.find('/10S') == 6:
            triac.value(1)
            time.sleep(10)
            triac.value(0)
            relayState=0
        if request.find('/S') == 6:
            relayState=1
            vauhti=eval(request[8]+request[9])
            tim.deinit()
            print('vauhti=',vauhti)
            set_speed(vauhti)
        if request.find('/LED/ON') == 6:
            SininenLedi.value(0)
        if request.find('/LED/OFF') == 6:
            SininenLedi.value(1)
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError:
        buttoni() 
"""



