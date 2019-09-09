#!/usr/bin/python

import sys, time, _thread

items = [2,5,1,3,0]


def sleepit(val):
    time.sleep(val/10)
    print(val)


[_thread.start_new_thread(sleepit,(a,)) for a in items]

while 1:
   pass