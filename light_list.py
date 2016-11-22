from lifxlan import Light
import sys

#Living Room Lights
L1=Light("MAC", "IP")
L2=Light("MAC", "IP")
L3=Light("MAC", "IP")
L4=Light("MAC", "IP")
L=(L1,L2,L3,L4)

#Kitchen Lights
K1=Light("MAC", "IP")
K2=Light("MAC", "IP")
K3=Light("MAC", "IP")
K4=Light("MAC", "IP")
K5=Light("MAC", "IP")
K6=Light("MAC", "IP")
K=(K1,K2,K3,K4)
Kalt=(K1,K2,K3,K4,K5,K6)

#Bedroom Lights
B1=Light("MAC", "IP")
B2=Light("MAC", "IP")
B=(B1,B2)

D=(K4,L1,L4)

All=(L1,L2,L3,L4,K1,K2,K3,K4,K5,K6,B1,B2)

def power_on(group):
    for x in group:
        x.set_power("on", rapid=True)

def power_down(group):
    for x in group:
        x.set_power("off", duration=15000)

