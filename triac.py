import network,time,machine,socket
from machine import Pin,Timer,ADC

triac=Pin(5, Pin.OUT)  
triac.value(0)

pot = ADC(Pin(15))
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v

sensor = ADC(Pin(4))
sensor.atten(ADC.ATTN_11DB)       #Full range: 3.3v

blue_led = Pin(2, Pin.OUT)  
blue_led.value(0)

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
    print(f"Motorspeed: {int(value)}")

if pot.read()>2000: # if throttle is at max: network connection
    import network_config
    while True:
        print('network')
        time.sleep(1)
        
zero_point=100

while pot.read()>zero_point:
    blue_led.value(1)
    time.sleep(0.1)
    blue_led.value(0)
    time.sleep(0.1)

blue_led.value(0)

SPEED=0   
PREV_SPEED=0
count=Timer(2)
def count_speed(t): #speed sensor from old walkman motor
    global SPEED
    SPEED=0.9 * (SPEED + 0.1*sensor.read())
def start_count():
    count.deinit()
    count.init(period=1, mode=Timer.PERIODIC, callback=count_speed)

previous_speed=0
stopped=True
while True:
  time.sleep(0.01)
  pot_value = pot.read()
  value=(pot_value-zero_point)
  print(value,int(SPEED))
  if pot_value<zero_point:
      if not stopped:
          stopped=True
          triac.value(0)
          tim.deinit() # This kills the background timer completely
          count.deinit()
          SPEED=0
  else:
      if stopped:
          triac.value(1)
          time.sleep(2*1./50) # initial boost for the motor
          triac.value(0)
          stopped=False
          start_count()
      if PREV_SPEED==SPEED: start_count()
      else: PREV_SPEED=SPEED
      diff=(value-SPEED)/10
      previous_speed=0.5*previous_speed + 0.5*diff
      set_speed(previous_speed)
      time.sleep(0.5)

