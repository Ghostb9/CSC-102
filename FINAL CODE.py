#Imports
import RPi.GPIO as GPIO
import time
import pygame
import tkinter as tk
from playsound import playsound
GPIO.setmode(GPIO.BCM)

#Sets sensors to GPIO board numbers
CUP_1 = 17
CUP_2 = 16
CUP_3 = 12
CUP_4 = 6
CUP_6 = 4
CUP_5 = 5

#Sets sensors to input
GPIO.setup(CUP_1, GPIO.IN)
GPIO.setup(CUP_2, GPIO.IN)
GPIO.setup(CUP_3, GPIO.IN)
GPIO.setup(CUP_4, GPIO.IN)
GPIO.setup(CUP_6, GPIO.IN)
GPIO.setup(CUP_5, GPIO.IN)

#Sets the servos to output
GPIO.setup(18, GPIO.OUT)#cup 1
GPIO.setup(19, GPIO.OUT)#cup 2  
GPIO.setup(20, GPIO.OUT)#cup 3
GPIO.setup(22, GPIO.OUT)#cup 5 
GPIO.setup(23, GPIO.OUT)#cup 6
GPIO.setup(21, GPIO.OUT)#cup 4

#Sets servos to GPIO board numbers
pwm_1 = GPIO.PWM(18, 25)#cup 1
pwm_2 = GPIO.PWM(19, 25)#cup 2
pwm_3 = GPIO.PWM(20, 25)#cup3
pwm_5 = GPIO.PWM(22, 25)#cup 5
pwm_6 = GPIO.PWM(23, 25)#cup 6
pwm_4 = GPIO.PWM(21, 25)# cup 4

#Goes to main page
def go_to_first():
    f1.pack()
    f2.pack_forget()
    f3.pack_forget()
    
#Goes to second Page
def go_to_second():
    f1.pack_forget()
    f3.pack_forget()
    f2.pack()
 
#Goes to third page   
def go_to_third():
    f3.pack()
    f1.pack_forget()
    
#Music 
def spins():
    pygame.init()
    pygame.mixer.music.load("spins.wav")
    pygame.mixer.music.play(-1)
    
#Music
def champ():
    pygame.init()
    pygame.mixer.music.load("kanye.wav")
    pygame.mixer.music.play(-1)

#Raise all Cups
def raiseCups():
    pwm_1.start(0)
    duty = 2
    while duty <=2:
        pwm_1.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_1 .start(0)
    pwm_2.start(0)
    duty = 2
    while duty <=2:
        pwm_2.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_2 .start(0)
    pwm_3.start(0)
    duty = 2
    while duty <=2:
        pwm_3.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_3.start(0)
    pwm_4.start(0)
    duty = 2
    while duty <=2:
        pwm_4.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_4.start(0)
    pwm_5.start(0)
    duty = 2
    while duty <=2:
        pwm_5.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_5.start(0)
    pwm_6.start(0)
    duty = 2
    while duty <=2:
        pwm_6.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_6.start(0)
    
#Main play function
def play():
    time.sleep(5)
    x=1
    while x < 8:
        if GPIO.input(CUP_1):
            print ("motion detected")
            playsound("sound.wav")
            pwm_1.start(0)
            duty = 2
            while duty <=8:
                pwm_1.ChangeDutyCycle(duty)
                time.sleep(1)
                duty= duty +1
            pwm_1 .start(0)
            x += 1
        elif GPIO.input(CUP_2):
            print ("motion detected")
            playsound("sound.wav")
            pwm_2.start(0)
            duty = 2
            while duty <=8:
                pwm_2.ChangeDutyCycle(duty)
                time.sleep(1)
                duty= duty +1
            pwm_2 .start(0)
            x += 1
        elif GPIO.input(CUP_3):
            print ("motion detected")
            playsound("sound.wav")
            pwm_3.start(0)
            duty = 2
            while duty <=8:
                pwm_3.ChangeDutyCycle(duty)
                time.sleep(1)
                duty= duty +1
            pwm_3 .start(0)
            x += 1
        elif GPIO.input(CUP_4):
            print ("motion detected")
            playsound("sound.wav")
            pwm_4.start(0)
            duty = 2
            while duty <=8:
                pwm_4.ChangeDutyCycle(duty)
                time.sleep(1)
                duty= duty +1
            pwm_4 .start(0)
            x += 1
        elif GPIO.input(CUP_5):
            print ("motion detected")
            playsound("sound.wav")
            pwm_5.start(0)
            duty = 2
            while duty <=8:
                pwm_5.ChangeDutyCycle(duty)
                time.sleep(1)
                duty= duty +1
            pwm_5 .start(0)
            x += 1
        elif GPIO.input(CUP_6):
            print ("motion detected")
            playsound("sound.wav")
            pwm_6.start(0)
            duty = 2
            while duty <=8:
                pwm_6.ChangeDutyCycle(duty)
                time.sleep(1)
                duty= duty +1
            pwm_6 .start(0)
            x += 1
        elif x == 4:
            go_to_second()
        else:
            print("ready")
    exit()
    
#Makes Triagnle pattern
def triangle():
    pwm_1.start(0)
    duty = 2
    while duty <=8:
        pwm_1.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_1 .start(0)
    pwm_2.start(0)
    duty = 2
    while duty <=8:
        pwm_2.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_2 .start(0)
    pwm_3.start(0)
    duty = 2
    while duty <=8:
        pwm_3.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_3.start(0)
    pwm_4.start(0)
    duty = 2
    while duty <=8:
        pwm_4.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_4.start(0)
    pwm_5.start(0)
    duty = 2
    while duty <=8:
        pwm_5.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_5.start(0)
    pwm_6.start(0)
    duty = 2
    while duty <=8:
        pwm_6.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_6.start(0)
    pwm_6.start(0)
    duty = 2
    while duty <=2:
        pwm_6.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_6.start(0)
    pwm_5.start(0)
    duty = 2
    while duty <=2:
        pwm_5.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_5.start(0)
    pwm_4.start(0)
    duty = 2
    while duty <=2:
        pwm_4.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_4.start(0)
    play()
    
#Makes cross pattern
def diamond():
    pwm_1.start(0)
    duty = 2
    while duty <=8:
        pwm_1.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_1 .start(0)
    pwm_2.start(0)
    duty = 2
    while duty <=8:
        pwm_2.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_2 .start(0)
    pwm_3.start(0)
    duty = 2
    while duty <=8:
        pwm_3.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_3.start(0)
    pwm_4.start(0)
    duty = 2
    while duty <=8:
        pwm_4.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_4.start(0)
    pwm_5.start(0)
    duty = 2
    while duty <=8:
        pwm_5.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_5.start(0)
    pwm_6.start(0)
    duty = 2
    while duty <=8:
        pwm_6.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_6.start(0)
    pwm_2.start(0)
    duty = 2
    while duty <=2:
        pwm_2.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_2.start(0)
    pwm_5.start(0)
    duty = 2
    while duty <=2:
        pwm_5.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_5.start(0)
    pwm_4.start(0)
    duty = 2
    while duty <=2:
        pwm_4.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_4.start(0)
    pwm_6.start(0)
    duty = 2
    while duty <=2:
        pwm_6.ChangeDutyCycle(duty)
        time.sleep(1)
        duty= duty +1
    pwm_6.start(0)
    play()
    exit()

master = tk.Tk()

 

#Starting Page
f1 = tk.Frame(master)
l1 = tk.Label(f1, text="")
l1.pack()
b1 = tk.Button(f1,height = 10, width = 40, text="Play", command=play)
b1.pack()
b3 = tk.Button(f1,height = 10, width = 40, text="Rerack", command=go_to_second)
b3.pack()
b5 = tk.Button(f1,height = 10, width = 40, text="Raise Cups", command=raiseCups)
b5.pack()
b4 = tk.Button(f1,height = 10, width = 40, text="Music", command=go_to_third)
b4.pack()

#Rerack Page

f2 = tk.Frame(master)
l3 = tk.Button(f2, height = 10, width = 40,text="Triangle", command = triangle )
l3.pack()
l4 = tk.Button(f2,height = 10, width = 40, text="Cross", command = diamond )
l4.pack()
b2 = tk.Button(f2, height = 10, width = 40,text="Return Home", command=go_to_first)
b2.pack()

#Music page

f3 = tk.Frame(master)
l4 = tk.Label(f3, text="")
l4.pack()
w2 = tk.Button(f3, height = 10, width = 40, text="The Spins", command = spins )
w2.pack()
w3 = tk.Button(f3, height = 10, width = 40,text="Champion", command = champ )
w3.pack()
w4 = tk.Button(f3, height = 10, width = 40,text="Return Home", command=go_to_first)
w4.pack()
master.geometry("5000x1000")

#Shows first frame

f1.pack()

master.mainloop()
        
        
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 