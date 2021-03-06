#!/usr/bin/python2

import sys
import io
import re
import os
#from termcolor import colored, cprint
from time import sleep

def usage():
    print "Usage:  %s" % os.path.basename(sys.argv[0])
	
# For loading executable PRU code
def setup_pru( code_to_load ):
	# load code now

def send_to_pru( location, data):
	# send data to location in PRU DDR
	
def setup_pwm( period_ns ):
    # make sure device tree overlay is loaded
	# gotta fix the overlay to match the one i've actually been using but haven't put in the repository yet, so this is all broken for now
    with open('/sys/devices/bone_capemgr.9/slots', 'a+') as slots:
        matches = 0
        for line in slots:
            if re.match(".*MPPT3", line):
                print line
                matches +=1
                break 
        if matches:
            print 'PWM overlay looks to be already loaded'
        else:
            print 'Trying to load the PWM overlay'
            slots.write('MPPT3')
        
		for line in slots:
            if re.match(".*iio", line):
                print line
                matches +=1
                break 
        if matches:
            print 'AIN overlay looks to be already loaded'
        else:
            print 'Trying to load the AIN overlay'
#            slots.write('cape-bone-iio') #fill this with analog helper DTO name if we're even using that
			
	    for line in slots:
            if re.match(".*PRU", line):
                print line
                matches +=1
                break 
        if matches:
            print 'PRU overlay looks to be already loaded'
        else:
            print 'Trying to load the PRU overlay'
            slots.write('PRU') # fill with PRU DTO name
			

#def setup_ain():
    # gotta buy some I2C or SPI current sensors and figure out how to talk to them

# Set correct PWM mode: symmetric, A triggers above threshold, B triggers below
	with open('prucode.p', 'r+') as prucode:
		setup_pru(prucode)
		# run it
	# load parameters into DDR...
	# build mode registers
	send_to_pru(TBCTLA, parameters)
	
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
