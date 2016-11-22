#!/usr/bin/env python



#imports
import RPi.GPIO as GPIO

from rec import *

import eiscp

import time

from light_list import *

from bright import *

import threading

print "Libriaries Imported"


#GPIO config
K_PIN_UP=24
K_PIN_DN=25
GPIO.setmode(GPIO.BCM)
GPIO.setup(K_PIN_UP, GPIO.IN)
GPIO.setup(K_PIN_DN, GPIO.IN)
print "GPIO Configured"
print ""

Move=20
if GPIO.input(K_PIN_UP)==1:
        Move=20


receiver = eiscp.eISCP('IP')
print "receiver defined"
print ""
def check(receiver):
        if receiver.command('system-power query') == ('system-power', 'on'):
                return "on"
        else:
                return "off"

def check(receiver):
        
        if receiver.command('system-power query') == ('system-power', 'on'):
                return True
        else:
                return False

receiver_state=check(receiver)

if GPIO.input(K_PIN_DN)==1:
        power_on(K)
        
print "check defined"
print ""

def remain(var):
  
        if var <0:
                var=0
        return var *10

#shutdown process
def NO_MOTION(K_PIN_DN):
        import time
                
        global Move
            
        while True:
                        
                
                if GPIO.input(K_PIN_DN)==1 and receiver_state==False:
                        Move=20
                        print " clock reset to 200 seconds"
                        print ""

                if GPIO.input(K_PIN_DN)==0 and Move >-10:
                        Move-=1 
                        print "decremented 10 seconds"
                        
                        print ""
                if Move >0:
                        
                        print "movement detected in Kitchen"
                        print  "%s seconds until lights turn off in Kitchen" % (remain(Move))
                        time.sleep(10)
                        pass
                if Move <1 and Move >-4:
                        try:
                                power_down(K)
                                        
                                print "Turning off lights in Kitchen"
                        
                        except:
                                print "exception caught"
                                pass
               
                                
        


print "NO_MOTION function defined"
print ""
def MOTION(K_PIN_UP):
        print "bitch please..."
        try:
                if GPIO.input(K_PIN_UP)==1:
                        power_on(K)
        except:
                time.sleep(1)
                if GPIO.input(K_PIN_UP)==1:
                        power_on(K)
        


                
print "MOTION function defined"
print ""     
# power up process
#set PIR to multi-detect / 2 Minute delay def MOTION(K_PIN_UP):


off = threading.Thread(target=NO_MOTION, name= "off", args=(K_PIN_DN,))

off.daemon=False

print "off defined"



off.start()


GPIO.add_event_detect(K_PIN_UP, GPIO.RISING, callback=MOTION)

print threading.enumerate()



#raw_input()
