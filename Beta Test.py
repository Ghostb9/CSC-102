import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_PIR= 17
GPIO.setup(GPIO_PIR, GPIO.IN)
GPIO.setup(16, GPIO.OUT)
pwm = GPIO.PWM(16, 25)
x=1
time.sleep(5)
while x == 1:
    if GPIO.input(GPIO_PIR):
        print ("motion detected")
        pwm.start(0)
        duty = 2
        while duty <=12:
            pwm.ChangeDutyCycle(duty)
            time.sleep(1)
            duty= duty +1
        pwm.start(0)
        x += 1
    else:
        print("ready")