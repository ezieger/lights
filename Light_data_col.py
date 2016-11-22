#!/usr/bin/env python



import eiscp
from bright import *
from light_list import *
import threading
import time

receiver = eiscp.eISCP('IP')
print "receiver defined"
print ""

def check(receiver):
        if receiver.command('system-power query') == ('system-power', 'on'):
                return "on"
        else:
                return "off"

def adjust_brightness(room):
        try:
                if check(receiver)=="off":
                        group_bright(room, 59441, 100)
                        print "receiver off... brightness set to full"
                        print ""  
                else:
                        group_bright(room, 9000, 100)
                        print " receiver on... brightness set to movie-mode"
                        print ""
                sleep(10)
                print "sleeping 10"
        except:
                print "thing happened"
                pass
        
def bright_worker(rm1):
    while True:
        adjust_brightness(rm1)
        time.sleep(30)

bw = threading.Thread(target=bright_worker, name="bright_worker", args=(K,))

bw.daemon=False

bw.start()

"""def rec_collector(receiver):
    while True:
        try:
            with open('rec_data.txt', 'w') as outfile:
                json.dump(check(receiver), outfile)
        except:
            time.sleep(2)
            pass
        time.sleep(10)


rec_check= threading.Thread(target=check, name="rec_collector", args=(receiver,))

"""
            
    
