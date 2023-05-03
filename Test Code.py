import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)
pwm = GPIO.PWM(16, 25)

pwm.start(0)
duty = 2
while duty <=12:
    pwm.ChangeDutyCycle(duty)
    time.sleep(1)
    duty= duty +1
   
pwm.ChangeDutyCycle(7)
pwm.start(0)