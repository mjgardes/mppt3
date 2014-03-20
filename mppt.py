#!/usr/bin/python2

import sys
import io
import re
import os
#from termcolor import colored, cprint
from time import sleep

def usage():
    print "Usage:  %s" % os.path.basename(sys.argv[0])

def setup_pwm( period_ns ):
    # make sure device tree overlay is loaded
    with open('/sys/devices/bone_capemgr.9/slots', 'a+') as slots:
        matches = 0
        for line in slots:
            if re.match(".*MPPT3", line):
                print "warning: device tree overlay already loaded. check compatibility yourself."
                matches +=1
                break 
        if matches:
            print 'overlay loaded that claims to be compatible'
        else:
            print 'attempting to load our overlay'
            slots.write('MPPT3')
                
    # make sure that pwms are exported
    pwm_num = 0
    for i in os.listdir('/sys/class/pwm'):
        if re.match('pwm[0-9]', i):
            pwm_num += 1
    if pwm_num == 0:
        for i in ['0', '1']:
            with open('/sys/class/pwm/export', 'w') as exports:
                exports.write(i)
            print 'exported pwm%s' % i
    elif pwm_num == 2 :
        print "pwm interfaces exported before i got to it.  continue at your own risk."
    else:
        print "something is wrong with the pwm interfaces.  you should probably reboot."
        
    # make sure pwm period matches configuration.  if not possible, request a reboot and die
    # make sure DC is 0 and one output has inverse polarity
    # run man, run

#def setup_ain():
    # probably just bake the pin names in for now
    # make sure that the ain DT overlay is loaded
    # i think there's a module that needs loaded too

#def request_duty( duty_ns ):

#def request_diff( posAIN, negAIN ):

#def request_eff( mean, sigma ):

def main():
    args = sys.argv[1:]
    if "-h" in args or "--help" in args:
        usage()
        sys.exit(2)
    setup_pwm( 7692 )
#    request_duty(769)  # or grab last known good setting from disk
    # fall into perturb and observe loop
#    while True:
        # read analog inputs
        # compute efficiency and standard deviation
        # log the data
        # "randomly" tweak the duty cycle, rinse, repeat
        # read analog inputs
        # compute if the mean new eff is significantly better than the old
        # if not request a return to the old
        # take a nap

if __name__ == '__main__':
    main()
