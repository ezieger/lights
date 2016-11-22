
from lifxlan import *
from light_list import *
def bright(lt,val, speed):
  num=lt.get_color()
  return lt.set_color([num[0],num[1],val,num[3]], speed*1000)

def group_bright(group, val, speed):
  for x in group:
    bright(x, val, speed)

def power_low(group, val, speed):
    for x in group:
        bright(x, val, speed)
        x.set_power("on", duration=speed*10)

#group-bright(K, 30)

