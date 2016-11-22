#!/usr/bin/env python


#imports
import RPi.GPIO as GPIO

import eiscp

import time

from bright import *

from light_list import *

import threading

print "Libriaries Imported"



#GPIO config
L_PIN_UP=22
L_PIN_DN=23
GPIO.setmode(GPIO.BCM)
GPIO.setup(L_PIN_UP, GPIO.IN)
GPIO.setup(L_PIN_DN, GPIO.IN)
print "GPIO Configured"
print ""
if GPIO.input(L_PIN_UP)==1:
        Move=20
        On_Move=20
else:
        Move=0
        On_Move=0
        
print "move defined"
#shutdown process

receiver = eiscp.eISCP('IP')
print "receiver defined"
print ""

def remain(var):
  
        if var <0:
                var=0
        return var *10

def check(receiver):
        
        try:
                if receiver.command('system-power query') == ('system-power', 'on'):
                        return True
                else:
                        return False
        except:
                print "receiver unavailable"
                sleep(2)
                if receiver.command('system-power query') == ('system-power', 'on'):
                        return True
                else:
                        return False

                
if GPIO.input(L_PIN_DN)==1:
        power_on(L)
        
# NEXT STEPSS!!  REMOVE DAEMON ATTRIBUTE from off thread.  THEN add a  loop to the thread worker to restart the off loop
def NO_MOTION(L_PIN_DN):
        import time
        global Move

        while True:
                global Move

                print "rerunning loop"
                print ""
                

                
                if GPIO.input(L_PIN_DN)==1 and check(receiver)==False:
                        Move=20
                        print "move set to 20"
                        print""
                if check(receiver)==True:
                        Move=0
                        print "Move is %s" % (Move)

                        print "move set to 0 per receiver state"
                        print""
                if GPIO.input(L_PIN_DN)==0:
                        Move= Move-1
                        print "Move is %s" % (Move)

                        print "move decremented by 1 per Pin down"
                        print""
                if Move >0:
                        
                        #print "movement detected in livingroom"
                        print""
                        print  "%s seconds until lights turn off in livingroom" % (remain(Move))
                        print""
                time.sleep(10)
                        
                if Move <1 and Move >-4:
                        print "trying move test"
                        print ""
                        print "Move is %s" % (Move)
                        try:
                                power_down(L)    
                                print "Turning off lights in living room"
                                print""
                        except:
                                print "exception caught"
                                print""
                                pass
                
def MOTION(L_PIN_UP):
        try:
                global Move

                if check(receiver)==False:
                        power_on(L)
                        print "movement detected in livingroom"
                        Move = 20
        except:
                print "exception caught in MOTION"
                time.sleep(5)
                if check(receiver)==False:
                        power_on(L)

                        print "movement detected in livingroom"

        #elif check(receiver)== True:
        #        power_down(L)
        #        print "receiver on powering down"
        #        print ""
                
                
print "MOTION function defined"
print ""     

#receiver_state=check(receiver)
"""def rcheck(receiver):
        global receiver_state
        
        while Move:
                receiver_state=check(receiver)
                print receiver_state
                global receiver_state
                print receiver_state
                sleep(10)
                """
GPIO.add_event_detect(L_PIN_UP, GPIO.RISING, callback=MOTION)

off = threading.Thread(target=NO_MOTION, name="off", args=(L_PIN_DN,))

off.daemon=False
#rec_check=threading.Thread(target=rcheck, name="rec_check", args=(receiver,))

off.start()

"""def Thread_worker(t):
        #t=[t1,t2]
        import time
        while 0==0:
                #for x in t:
                if t.isAlive()!=True:
                        t.join()
                        time.sleep(10)
                        print threading.enumerate()
                        print "thread recycled"
                        print ""

#                if t2.isAlive()!=True:
#                        t2.start()
#                        print t1 +"recycled"
#                        print ""
        
"""
                

        
#checker = threading.Thread(target=Thread_worker, name="thread_worker", args=(off,))


#checker.start()
#print "checker started"
print threading.enumerate()

#print checker.isAlive()

#while         

#raw_input()
