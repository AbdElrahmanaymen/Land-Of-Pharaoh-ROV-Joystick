#importing needed libraries
from math import sin, cos 
import requests
import pygame
import pickle


#Some global variables needed later
motors_pwm = [0, 0, 0, 0, 0, 0]
motors_dir = [0, 0, 0, 0, 0, 0] 

MR1_PWM = 0
MR1_D = 0
MR1_ARM = 0

Speed_value = 255
MID_POINT = 0.2
MAX_POINT = 1
MIN_POINT = -1


#Define all joystick process here
class joystickClass:

    #initliazing joystick depend joystick id were given
    def __init__(self, joyNum):
        print("INIT SAYS.....")
        self.joy = pygame.joystick.Joystick(joyNum) 
        self.joy.init()
        print("DONE INIT")

    #Reading joystick values
    def execute(self, event):
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.JOYAXISMOTION:
            if event.axis ==0 or event.axis ==1:
                self.axis01()
            elif event.axis ==2:
                self.axis2()
            elif event.axis ==3 or event.axis ==4:
                self.axis34()
        elif event.type == pygame.JOYHATMOTION:
            self.hat(event.value)
        elif event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                self.but0()
            elif event.button == 1:
                self.but1() 
            elif event.button == 2:
                self.but2()
            elif event.button == 3:
                self.but3()
            elif event.button == 4:
                self.but4()
            elif event.button == 5:
                self.but5()
            elif event.button == 6:
                self.but6()
            elif event.button == 7:
                self.but7()
            elif event.button == 8:
                self.but8()
            elif event.button == 9:
                self.but9()

    #define joystick buttons and joys
    def setButtonMap(self,but):
        print("press "+but+"\n")
        self.buttunMap[event.button]=but

    ###Buttons and joys process###
    def but0(self):
        # A Button in Xbox 360 Joystick
        print("Button 0 presed")
    def but1(self):
        # B Button in Xbox 360 Joystick
        print("Button 1 presed")
    def but2(self):
        # X Button in Xbox 360 Joystick
        print("Button 2 presed")
    def but3(self):
        # Y Button in Xbox 360 Joystick
        print("Button 3 presed")
    def but4(self):
        # LB Button in Xbox 360 Joystick
        print("Button 4 presed")
    def but5(self):
        # RB Button in Xbox 360 Joystick
        print("Button 5 presed")
    def but6(self):
        # Back Button in Xbox 360 Joystick
        print("Button 6 presed")
    def but7(self):
        # Start Button in Xbox 360 Joystick
        print("Button 7 presed")
    def but8(self):
        # Joy1 press Button in Xbox 360 Joystick
        print("Button 8 presed")
    def but9(self):
        # Joy2 press Button in Xbox 360 Joystick
        print("Button 9 presed")
    
    
    def hat(self,value):
        #code here
        if value==(0,1):
            MR1_PWM = 255
            MR1_D = 1
            print("Micro ROV Forward")

        elif value==(0,-1):
            MR1_PWM = 255
            MR1_D = 0
            print("Micro ROV Backward")

        elif value==(0,0):
            MR1_PWM = MR1_D = 0

        elif value==(1,0):
            MR1_ARM = 1
            print("Micro ROV Arm opening")

        elif value==(-1,0):
            MR1_ARM = 0
            print("Micro ROV Arm closeing")

    #Processing of Joy 1 in joystick to move the ROV (Forward, Backward, Left, Right)
    def axis01(self):
        x=round(self.joy.get_axis(0),1)
        y=round(self.joy.get_axis(1),1)
        if y < -0.2:
            speed = round(abs(calcSpeed(y, 0, 1, 0, 255)))
            motors_pwm[0] = motors_pwm[1] = speed
            motors_dir[0] = 1
            motors_dir[1] = 1

            motors_pwm[2] = motors_pwm[3] = speed
            motors_dir[2] = 0
            motors_dir[3] = 0
            print(motors_pwm)
            print(motors_dir)
            print("ROV Forward")

        elif y > MID_POINT:
            speed = round(abs(calcSpeed(y, 0, 1, 0, 255)))
            motors_pwm[0] = motors_pwm[1] = speed
            motors_dir[0] = 0
            motors_dir[1] = 0

            motors_pwm[2] = motors_pwm[3] = speed
            motors_dir[2] = 1
            motors_dir[3] = 1
            print(motors_pwm)
            print(motors_dir)
            print("ROV Backward")

        elif x > MID_POINT:
            speed = round(abs(calcSpeed(x, 0, 1, 0, 255)))
            motors_pwm[0] = motors_pwm[2] = speed
            motors_dir[0] = 1
            motors_dir[2] = 1

            motors_pwm[1] = motors_pwm[3] = speed
            motors_dir[1] = 0
            motors_dir[3] = 0
            print(motors_pwm)
            print(motors_dir)
            print("ROV Right")

        elif x < -0.2:
            speed = round(abs(calcSpeed(x, 0, 1, 0, 255)))
            motors_pwm[0] = motors_pwm[2] = speed
            motors_dir[0] = 0
            motors_dir[2] = 0

            motors_pwm[1] = motors_pwm[3] = speed
            motors_dir[1] = 1
            motors_dir[3] = 1
            print(motors_pwm)
            print(motors_dir)
            print("ROV Left")
        
        else:
            motors_pwm[0] = motors_pwm[1] = motors_pwm[2] = motors_pwm[3] = 0

    #Processing of Joy 2 to rotate ROV(Left, Right)
    def axis34(self):
        x=round(self.joy.get_axis(4),1)

        if x > MID_POINT:
            speed = round(abs(calcSpeed(x, 0, 1, 0, 255)))
            motors_pwm[1] = motors_pwm[2] = speed
            motors_dir[1] = 1
            motors_dir[2] = 1


            motors_pwm[0] = motors_pwm[3] = speed
            motors_dir[0] = 1
            motors_dir[3] = 1

            print(motors_pwm)
            print(motors_dir)
            print("ROV Rotate Right")

        elif x < -0.2:
            speed = round(abs(calcSpeed(x, 0, 1, 0, 255)))
            motors_pwm[1] = motors_pwm[2] = speed
            motors_dir[1] = 0
            motors_dir[2] = 0

            motors_pwm[0] = motors_pwm[3] = speed
            motors_dir[0] = 0
            motors_dir[3] = 0

            print(motors_pwm)
            print(motors_dir)
            print("ROV Rotate Left")

        else:
            motors_pwm[0] = motors_pwm[1] = motors_pwm[2] = motors_pwm[3] = 0

    def axis2 (self):
        x=round(self.joy.get_axis(2),1)

        if x < -0.2:
            speed = round(abs(calcSpeed(x, 0, 1, 0, 255)))
            motors_pwm[4] = motors_pwm[5] = speed
            motors_dir[4] = 1
            motors_dir[5] = 0
            print(motors_pwm)
            print(motors_dir)
            print("ROV Up")

        elif x > MID_POINT:
            speed = round(abs(calcSpeed(x, 0, 1, 0, 255)))
            motors_pwm[4] = motors_pwm[5] = speed
            motors_dir[4] = 0
            motors_dir[5] = 1
            print(motors_pwm)
            print(motors_dir)
            print("ROV Down")
        else:
            motors_pwm[4] = motors_pwm[5] = 0

    ######End of Buttons and Joys process######


#Mapping from joy reading to motor speed(PWM) in range 0 to 255
def calcSpeed(joyAxis, joyRead1, joyRead2, mapPoint1, mapPoint2):
    return (mapPoint1 + ((joyAxis - joyRead1) * (mapPoint2 - mapPoint1) / (joyRead2 - joyRead1)))

#Send data into web packets to flask server through get request
def send(PARAMS, subPath="joy"):
    r = requests.post(url = "http://127.0.0.1:5000/"+subPath, params = {'joystick':PARAMS})
    

if __name__ == '__main__':
    pygame.init()
    running = True
    joy1 = joystickClass(0)
    x=""
    while running:
        for event in pygame.event.get():
            joy1.execute(event)
            Data = "A" + str(motors_pwm[0]) + "B" + str(motors_pwm[1]) + "C" + str(motors_pwm[2]) + "D" + str(motors_pwm[3]) + "E" + str(motors_pwm[4]) + "F" + str(motors_pwm[5]) + "H" + str(MR1_PWM) + "I" + str(motors_dir[0]) + "J" + str(motors_dir[1]) + "K" + str(motors_dir[2]) + "L" + str(motors_dir[3]) + "M" + str(motors_dir[4]) + "N" + str(motors_dir[5]) + "O" + str(MR1_D) + "T" + "Z"
            send(Data)

    pygame.quit()
