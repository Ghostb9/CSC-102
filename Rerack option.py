import tkinter as tk
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO_PIR= 17
GPIO.setup(GPIO_PIR, GPIO.IN)
GPIO.setup(16, GPIO.OUT)
pwm = GPIO.PWM(16, 25)
x=1
time.sleep(5)

def go_to_first():
    f1.pack()
    f2.pack_forget()
def go_to_second():
    f1.pack_forget()
    f2.pack()
def stoplight():
    exit()
def triangle():
    exit()
def diamond():
    exit()

master = tk.Tk()

#STARTING PAGE
f1 = tk.Frame(master)
l1 = tk.Label(f1, text="")
l1.pack()
b1 = tk.Button(f1, text="Rerack", command=go_to_second)
b1.pack()

#RERACK PAGE
f2 = tk.Frame(master)
l2 = tk.Button(f2, text="Stoplight", command =stoplight )
l2.pack()
l3 = tk.Button(f2, text="Triangle", command = triangle )
l3.pack()
l4 = tk.Button(f2, text="Diamond", command = diamond )
l4.pack()
b2 = tk.Button(f2, text="Return Home", command=go_to_first)
b2.pack()

master.geometry("320x200")
# show first frame
f1.pack()

master.mainloop()

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