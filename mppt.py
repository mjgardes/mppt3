#!/usr/bin/python2

def usage():
    print "Usage:  %s" % os.path.basename(sys.argv[0])

def setup_pwm( period_ns ):
    # make sure device tree overlay is loaded
    # make sure that pwms are exported
    # make sure pwm period matches configuration.  if not possible, request a reboot and die
    # make sure DC is 0 and one output has inverse polarity
    # run man, run

def setup_ain():
    # probably just bake the pin names in for now
    # make sure that the ain DT overlay is loaded
    # i think there's a module that needs loaded too

def request_duty( duty_ns ):

def request_diff( posAIN, negAIN ):

def request_eff( mean, sigma ):

def main():
    args = sys.argv[1:]
    if "-h" in args or "--help" in args:
        usage()
        sys.exit(2)
    setup_pwm( 7692 )
    request_duty(769)  # or grab last known good setting from disk
    # fall into perturb and observe loop
    while True:
        # read analog inputs
        # compute efficiency and standard deviation
        # log the data
        # "randomly" tweak the duty cycle, rinse, repeat
        # read analog inputs
        # compute if the mean new eff is significantly better than the old
        # if not request a return to the old
        # take a nap
