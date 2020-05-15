import RPi.GPIO as GPIO

from time import sleep


def drive_forwards(time, power, setup = False):
    """
    Drive fowards for time seconds at power % of max power.
    
    If setup is False, board and motor setup will be skipped.
    """

    Motor1A = 16
    Motor1B = 18
    Motor1E = 22

    Motor2A = 19
    Motor2B = 21
    Motor2E = 23

    if setup is True:
        
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(Motor1A,GPIO.OUT)
        GPIO.setup(Motor1B,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)

        GPIO.setup(Motor2A,GPIO.OUT)
        GPIO.setup(Motor2B,GPIO.OUT)
        GPIO.setup(Motor2E,GPIO.OUT)
        
    pwm1 = GPIO.PWM(Motor1E, 100)
    pwm2 = GPIO.PWM(Motor2E, 100)

    print("Going forwards at {}%...".format(power))
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)

    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
    
    pwm1.start(power)
    pwm2.start(power)

    sleep(time)
    
    print("Stopping forwards drive")
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)
    pwm1.stop()
    pwm2.stop()

    if setup is True:
        GPIO.cleanup()
    

def drive_backwards(time, power, setup = False):
    """
    Drive backwards for time seconds at power % of max power.
    
    If setup is False, board and motor setup will be skipped.
    """

    Motor1A = 16
    Motor1B = 18
    Motor1E = 22

    Motor2A = 19
    Motor2B = 21
    Motor2E = 23
    
    if setup is True:
    
        GPIO.setmode(GPIO.BOARD)

        GPIO.setup(Motor1A,GPIO.OUT)
        GPIO.setup(Motor1B,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)

        GPIO.setup(Motor2A,GPIO.OUT)
        GPIO.setup(Motor2B,GPIO.OUT)
        GPIO.setup(Motor2E,GPIO.OUT)
        
    pwm1 = GPIO.PWM(Motor1E, 100)
    pwm2 = GPIO.PWM(Motor2E, 100)

    print("Going backwards at {}%...".format(power))
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)

    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
    
    pwm1.start(power)
    pwm2.start(power)

    sleep(time)
    
    print("Stopping forwards drive")
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)
    pwm1.stop()
    pwm2.stop()

    if setup is False:
        GPIO.cleanup()
        
    
def turn(direction, time, setup = False):
    """
    Turns cart in specified direction for time seconds.
    
    If setup is False, board and motor setup will be skipped.
    """
    
    if direction not in ['left', 'right']:
        raise ValueError('direction must be \'left\' or \'right\'')
    
    Motor1A = 16
    Motor1B = 18
    Motor1E = 22

    Motor2A = 19
    Motor2B = 21
    Motor2E = 23
    
    if setup is True:
    
        GPIO.setmode(GPIO.BOARD)
        
        GPIO.setup(Motor1A,GPIO.OUT)
        GPIO.setup(Motor1B,GPIO.OUT)
        GPIO.setup(Motor1E,GPIO.OUT)

        GPIO.setup(Motor2A,GPIO.OUT)
        GPIO.setup(Motor2B,GPIO.OUT)
        GPIO.setup(Motor2E,GPIO.OUT)
        
    pwm1 = GPIO.PWM(Motor1E, 100)
    pwm2 = GPIO.PWM(Motor2E, 100)

    print('Starting turn in {} direction...'.format(direction))    
    if direction == 'right':
                
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)

        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)

        pwm1.start(0)
        pwm2.start(100)
        
        sleep(time)
        
        pwm1.stop()
        pwm2.stop()

    else:
        
        GPIO.output(Motor1A,GPIO.HIGH)
        GPIO.output(Motor1B,GPIO.LOW)
        GPIO.output(Motor1E,GPIO.HIGH)

        GPIO.output(Motor2A,GPIO.HIGH)
        GPIO.output(Motor2B,GPIO.LOW)
        GPIO.output(Motor2E,GPIO.HIGH)

        pwm1.start(100)
        pwm2.start(50)
        
        sleep(time)
        
        pwm1.stop()
        pwm2.stop()
        
    print('Stopping {} turn'.format(direction))
    pwm1.stop()
    pwm2.stop()
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)
    
    GPIO.cleanup()

    
if __name__ == '__main__':
    
    drive_forwards(20, 100, True)
    
