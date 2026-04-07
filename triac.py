import network,time,machine,socket
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
#    goal_speed = round(value/5.-10)
    goal_speed = round(value/2.-25)
    if goal_speed==0: goal_speed=1
    print(f"Motor speed set to: {goal_speed}")

if pot.read()>2000: # kun kaasu on pohjassa: nettiyhteys
    import netti
    while True:
        print('netti')
        time.sleep(1)
        
Nollapiste=100

while pot.read()>Nollapiste:
    SininenLedi.value(1)
    time.sleep(0.1)
    SininenLedi.value(0)
    time.sleep(0.1)

SininenLedi.value(0)

Stopped=True

while True:
  pot_value = pot.read()
  print("raaka=",pot_value)
  time.sleep(0.1)
  if pot_value<Nollapiste:
    Stopped=True
    triac.value(0)
    tim.deinit() # This kills the background timer completely
  else:
    if Stopped:
      triac.value(1)
      time.sleep(2*1./50) #moottorille alkusykäys
      triac.value(0)
      Stopped=False
    range=(4000-Nollapiste)
    value=(pot_value-Nollapiste)/range
    value=int(range*(value**1.2))
    print(pot_value,value)
    set_speed(value/30)
