#!/home/pi/scripts
import eiscp
from bright import *

receiver = eiscp.eISCP('IP')
print "receiver defined"
print ""

def check(receiver):
        if receiver.command('system-power query') == ('system-power', 'on'):
                return "on"
        else:
                return "off"

def adjust_power(room):
        if check(receiver)=="on":
                power_down(room)
                print " receiver on... powering down lights in living room"
                print ""
        
                
def adjust_brightness(room):
        if check(receiver)=="off":
                group_bright(room, 59441, 100)
                print "receiver off... brightness set to full"
                print ""  
        else:
                group_bright(room, 9000, 100)
                print " receiver on... brightness set to movie-mode"
                print ""  
