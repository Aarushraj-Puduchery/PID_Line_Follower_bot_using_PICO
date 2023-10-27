#PID Line Follower Bot Code BY Aarushraj Puduchery
"""
IR sensors
0-6 ---> GP16,17,18,19,20,21,22
Left IR ---> GP26
Right IR --->GP27

MOTORs
M=Motor A=Right B=Left C=Control
PWM MAC ---> GP14
PWM MBC ---> GP15
MAF ---> GP2
MAR ---> GP3
MBF ---> GP4
MBR ---> GP5

Button
StartButton(RED)(SB) ---> GP6
Calibration or ShortDistance(Blue)(CB) ---> GP7
"""
from machine import Pin,PWM,I2C
from utime import sleep,sleep_ms
import sys
import ssd1306
#Setup
#oled
i2c = I2C(0, sda=Pin(0), scl=Pin(1))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
#Button
SB=Pin(5,Pin.IN,Pin.PULL_DOWN)
CB=Pin(4,Pin.IN,Pin.PULL_DOWN)
#Sensors
IRL=Pin(26,Pin.IN)
IR0=Pin(16,Pin.IN)
IR1=Pin(17,Pin.IN)
IR2=Pin(19,Pin.IN)
IR3=Pin(21,Pin.IN)
IR4=Pin(22,Pin.IN)
IRR=Pin(27,Pin.IN)
IRLV=0
IR0V=0
IR1V=0
IR2V=0
IR3V=0
IR4V=0
IRRV=0
IR_Sensors=[IRL,IR0,IR1,IR2,IR3,IR4,IRR]
IR_Values=[IRLV,IR0V,IR1V,IR2V,IR3V,IR4V,IRRV]
#Motors
MAF = Pin(6,Pin.OUT)
MAR = Pin(7,Pin.OUT)
MBF = Pin(8,Pin.OUT)
MBR = Pin(9,Pin.OUT)
MAC = PWM(Pin(14))
MBC = PWM(Pin(15))

MAC.freq(1000)
MBC.freq(1000)
MAV=0
MBV=0
#PID
POS = 0
error = 0
KpFile=open("KpValue.csv","r")
kp = float(KpFile.read())
KiFile=open("KiValue.csv","r")
ki = float(KiFile.read())
KdFile=open("KdValue.csv","r")
kd = float(KdFile.read())
P=0
I=0
D=0
PIDvalue=0
previousError=0
SetSpeed = 22512
Mode = 0
def ReadSensors():
    for i in range(0,7):
        if i==0 or i==6:
            IR_Values[i] = int(not (IR_Sensors[i].value()))
            continue
        IR_Values[i] = IR_Sensors[i].value()
    sleep(0.01)
        
def LinePosition():
    ReadSensors()
    global POS,Mode
    if   IR_Values[0] == 0 and IR_Values[1] == 0 and IR_Values[2] == 0 and IR_Values[3] == 0 and IR_Values[4] == 0 and IR_Values[5] == 1 and IR_Values[6] == 0:
        POS=4000
        Mode = 0
    elif IR_Values[0] == 0 and IR_Values[1] == 0 and IR_Values[2] == 0 and IR_Values[3] == 0 and IR_Values[4] == 1 and IR_Values[5] == 1 and IR_Values[6] == 0:
        POS=3500
        Mode = 0
    elif IR_Values[0] == 0 and IR_Values[1] == 0 and IR_Values[2] == 0 and IR_Values[3] == 0 and IR_Values[4] == 1 and IR_Values[5] == 0 and IR_Values[6] == 0:
        POS=3000
        Mode = 0
    elif IR_Values[0] == 0 and IR_Values[1] == 0 and IR_Values[2] == 0 and IR_Values[3] == 1 and IR_Values[4] == 1 and IR_Values[5] == 0 and IR_Values[6] == 0:
        POS=2500
        Mode = 0
    elif IR_Values[0] == 0 and IR_Values[1] == 0 and IR_Values[2] == 0 and IR_Values[3] == 1 and IR_Values[4] == 0 and IR_Values[5] == 0 and IR_Values[6] == 0:
        POS=2000
        Mode = 0
    elif IR_Values[0] == 0 and IR_Values[1] == 0 and IR_Values[2] == 1 and IR_Values[3] == 1 and IR_Values[4] == 0 and IR_Values[5] == 0 and IR_Values[6] == 0:
        POS=1500
        Mode = 0
    elif IR_Values[0] == 0 and IR_Values[1] == 0 and IR_Values[2] == 1 and IR_Values[3] == 0 and IR_Values[4] == 0 and IR_Values[5] == 0 and IR_Values[6] == 0:
        POS=1000
        Mode = 0
    elif IR_Values[0] == 0 and IR_Values[1] == 1 and IR_Values[2] == 1 and IR_Values[3] == 0 and IR_Values[4] == 0 and IR_Values[5] == 0 and IR_Values[6] == 0:
        POS=500
        Mode = 0
    elif IR_Values[0] == 0 and IR_Values[1] == 1 and IR_Values[2] == 0 and IR_Values[3] == 0 and IR_Values[4] == 0 and IR_Values[5] == 0 and IR_Values[6] == 0:
        POS=0
        Mode = 0
    elif IR_Values[0] == 0 and IR_Values[1] == 1 and IR_Values[2] == 1 and IR_Values[3] == 1 and IR_Values[4] == 0 and IR_Values[5] == 0 and IR_Values[6] == 0:
    #and IR_Values[1] == 0 and IR_Values[2] == 0 and IR_Values[3] == 0 and IR_Values[4] == 0 and IR_Values[5] == 0 and IR_Values[6] == 0 and IR_Values[7] == 0 and IR_Values[8] == 0:
        POS=2000
        Mode = 1
    elif IR_Values[0] == 0 and IR_Values[1] == 0 and IR_Values[2] == 0 and IR_Values[3] == 1 and IR_Values[4] == 1 and IR_Values[5] == 1 and IR_Values[6] == 0:
    #IR_Values[0] == 0 and IR_Values[1] == 0 and IR_Values[2] == 0 and IR_Values[3] == 0 and IR_Values[4] == 0 and IR_Values[5] == 0 and IR_Values[6] == 0 and IR_Values[7] == 0 and IR_Values[8] == 1:
        POS=2000
        Mode = 2
    elif IR_Values[0] == 0 and IR_Values[1] == 0 and IR_Values[2] == 0 and IR_Values[3] == 0 and IR_Values[4] == 0 and IR_Values[5] == 0 and IR_Values[6] == 0:
        POS = 2000
        Mode = 3
    elif IR_Values[0] == 0 and IR_Values[1] == 1 and IR_Values[2] == 1 and IR_Values[3] == 1 and IR_Values[4] == 1 and IR_Values[5] == 1 and IR_Values[6] == 0:
        POS=2000
        Mode = 4
    elif IR_Values[0] == 0 and IR_Values[1] == 0 and IR_Values[2] == 1 and IR_Values[3] == 1 and IR_Values[4] == 1 and IR_Values[5] == 0 and IR_Values[6] == 0:
    #or (IR_Values[0] == 0 and IR_Values[1] == 1 and IR_Values[2] == 1 and IR_Values[3] == 0 and IR_Values[4] == 1 and IR_Values[5] == 1 and IR_Values[6] == 0) or (IR_Values[0] == 0 and IR_Values[1] == 1 and IR_Values[2] == 1 and IR_Values[3] == 0 and IR_Values[4] == 0 and IR_Values[5] == 1 and IR_Values[6] == 0) or (IR_Values[0] == 0 and IR_Values[1] == 1 and IR_Values[2] == 0 and IR_Values[3] == 0 and IR_Values[4] == 1 and IR_Values[5] == 1 and IR_Values[6] == 0):
        POS=2000
        Mode = 5
    elif IR_Values[0] == 0 and IR_Values[1] == 1 and IR_Values[2] == 0 and IR_Values[3] == 1 and IR_Values[4] == 0 and IR_Values[5] == 0 and IR_Values[6] == 0:
        POS=2000
        Mode = 6
    elif IR_Values[0] == 0 and IR_Values[1] == 0 and IR_Values[2] == 0 and IR_Values[3] == 1 and IR_Values[4] == 0 and IR_Values[5] == 1 and IR_Values[6] == 0:
        POS=2000
        Mode = 7

def PIDControl():
    global kp,ki,kd,P,I,D,PIDvalue,previousError,SetSpeed,MAV,MBV
#     kp = 3
#     ki = 0.002
#     kd = 10
    #print("POS",POS)
#     print(kp)
#     print(ki)
#     print(kd)
    error = 2000 - POS
    
    P = error
    I = I + error
    D = error - previousError
    
    PIDvalue = (kp)*P + (ki)*I + (kd)*D
    previousError = error
    print("PID Value",PIDvalue)
    MAV = int(SetSpeed + PIDvalue)
    MBV = int(SetSpeed - PIDvalue)

    
    if MAV >= 35025:
        MAV = 33000
    if MAV < 0:
        MAV = 0
    if MBV >= 35025:
        MBV = 33000
    if MBV < 0:
        MBV = 0
    MBVT=str(MBV)
    MAVT=str(MAV)
    oled.text("MAV=", 0, 0)
    oled.text(MAVT, 35, 0)
    oled.text("MBV=", 0, 20)
    oled.text(MBVT, 35, 20)
    oled.show()
    oled.fill(0)
    #print(MBV)

def LeftTurn():
    oled.text("Left Turn", 0, 20)
    oled.show()
    oled.fill(0)
    #Stop()
    flag1 = 0
    while flag1 == 0:
        MAC.duty_u16((12500))
        MBC.duty_u16((12500))
        MAF.value(1)
        MAR.value(0)
        MBF.value(1)
        MBR.value(0)
        IR_Values[0] = IR_Sensors[0].value()
        if IR_Values[0] == 0:
            flag1 = 1
    while flag1 == 1:
        MAC.duty_u16((12500))
        MBC.duty_u16((12500))
        MAF.value(1)
        MAR.value(0)
        MBF.value(1)
        MBR.value(0)
        IR_Values[0] = IR_Sensors[0].value()
        if IR_Values[0] == 1:
            flag1 = 2
    while flag1 == 2:
        Stop()
        IR_Values[2] = IR_Sensors[2].value()
        IR_Values[3] = IR_Sensors[3].value()
        while IR_Values[2] == 0 and IR_Values[3] == 0:
            MAC.duty_u16((12500))
            MBC.duty_u16((12500))
            MAF.value(1)
            MAR.value(0)
            MBF.value(0)
            MBR.value(1)
            IR_Values[2] = IR_Sensors[2].value()
            IR_Values[3] = IR_Sensors[3].value()
        flag1 = 3
        #ReadSensors()
        #print("MIddle",IR_Values[4])
    #if IR_Values[4] == 1:
    Stop()
    Mode = 0
    print("Out From Turn")
     

def RightTurn():
    oled.text("Right Turn", 0, 20)
    oled.show()
    oled.fill(0)
    #Stop()
    flag2 = 0
    while flag2 == 0:
        MAC.duty_u16((12500))
        MBC.duty_u16((12500))
        MAF.value(1)
        MAR.value(0)
        MBF.value(1)
        MBR.value(0)
        IR_Values[6] = IR_Sensors[6].value()
        if IR_Values[6] == 0:
            flag2 = 1
    while flag2 == 1:
        MAC.duty_u16((12500))
        MBC.duty_u16((12500))
        MAF.value(1)
        MAR.value(0)
        MBF.value(1)
        MBR.value(0)
        IR_Values[6] = IR_Sensors[6].value()
        if IR_Values[6] == 1:
            flag2 = 2
    while flag2 == 2:
        Stop()
        IR_Values[3] = IR_Sensors[3].value()
        while IR_Values[3] == 0:
            MAC.duty_u16((12500))
            MBC.duty_u16((12500))
            MAF.value(0)
            MAR.value(1)
            MBF.value(1)
            MBR.value(0)
            #IR_Values[2] = IR_Sensors[2].value()
            IR_Values[3] = IR_Sensors[3].value()
        flag2 = 3
        #ReadSensors()
        #print("Middle",IR_Values[3])
    #if IR_Values[4] == 1:
    Stop()
    Mode = 0
    print("Out From Turn")

def BackTurn():
    oled.text("Back Turn", 0, 20)
    oled.show()
    oled.fill(0)
    #Stop()
    while IR_Values[3] == 0:
        MAC.duty_u16((12500))
        MBC.duty_u16((12500))
        MAF.value(0)
        MAR.value(1)
        MBF.value(1)
        MBR.value(0)
        IR_Values[3] = IR_Sensors[3].value()
        #ReadSensors()
        #print("MIddle",IR_Values[4])
    #if IR_Values[4] == 1:
    Stop()
    Mode = 0
    print("Out From Turn")

def CrossTurn():
    oled.text("Cross Turn", 0, 20)
    oled.show()
    oled.fill(0)
    flag3 = 0
    while flag3 == 0:
        MAC.duty_u16((12500))
        MBC.duty_u16((12500))
        MAF.value(1)
        MAR.value(0)
        MBF.value(1)
        MBR.value(0)
        IR_Values[6] = IR_Sensors[6].value()
        if IR_Values[6] == 0:
            flag3 = 1
    while flag3 == 1:
        MAC.duty_u16((12500))
        MBC.duty_u16((12500))
        MAF.value(1)
        MAR.value(0)
        MBF.value(1)
        MBR.value(0)
        IR_Values[6] = IR_Sensors[6].value()
        if IR_Values[6] == 1:
            flag3 = 2
    while flag3 == 2:
        Stop()
        while IR_Values[3] == 1:
            MAC.duty_u16((12500))
            MBC.duty_u16((12500))
            MAF.value(1)
            MAR.value(0)
            MBF.value(0)
            MBR.value(1)
            IR_Values[3] = IR_Sensors[3].value()
        flag3 = 3
    while flag3 == 3:
        IR_Values[3] = IR_Sensors[3].value()
        while IR_Values[3] == 0:
            MAC.duty_u16((12500))
            MBC.duty_u16((12500))
            MAF.value(1)
            MAR.value(0)
            MBF.value(0)
            MBR.value(1)
            IR_Values[3] = IR_Sensors[3].value()
            flag3 = 4
    while flag3 == 4:
        Stop()
        Mode = 0
        flag3 = 5

def YCross():
    oled.text("YCross Turn", 0, 20)
    oled.show()
    oled.fill(0)
    flag=0
    while flag == 0:
        MAC.duty_u16((12500))
        MBC.duty_u16((12500))
        MAF.value(1)
        MAR.value(0)
        MBF.value(1)
        MBR.value(0)
        ReadSensors()
        if IR_Values[0] == 0 and IR_Values[1] == 0 and IR_Values[2] == 0 and IR_Values[3] == 0 and IR_Values[4] == 0 and IR_Values[5] == 0 and IR_Values[6] == 0:
            flag = 1
    while flag == 1:
        Stop()
        while IR_Values[3] == 0:
            MAC.duty_u16((19500))
            MBC.duty_u16((19500))
            MAF.value(1)
            MAR.value(0)
            MBF.value(0)
            MBR.value(0)
            IR_Values[3] = IR_Sensors[3].value()
        flag = 2  
    Stop()
    Mode = 0
    
def AcuteLeft():
    oled.text("Acute Left Turn", 0, 20)
    oled.show()
    oled.fill(0)
    flag=0
    while flag == 0:
        MAC.duty_u16((12500))
        MBC.duty_u16((12500))
        MAF.value(0)
        MAR.value(1)
        MBF.value(1)
        MBR.value(0)
        ReadSensors()
        if IR_Values[0] == 0 and IR_Values[1] == 0 and IR_Values[2] == 0 and IR_Values[3] == 0 and IR_Values[4] == 0 and IR_Values[5] == 0 and IR_Values[6] == 0:
            flag = 1
    while flag == 1:
        Stop()
        while IR_Values[3] == 0:
            MAC.duty_u16((19500))
            MBC.duty_u16((19500))
            MAF.value(1)
            MAR.value(0)
            MBF.value(0)
            MBR.value(0)
            IR_Values[3] = IR_Sensors[3].value()
        flag = 2  
    Stop()
    Mode = 0

def AcuteRight():
    oled.text("Acute Right Turn", 0, 20)
    oled.show()
    oled.fill(0)
    flag=0
    while flag == 0:
        MAC.duty_u16((12500))
        MBC.duty_u16((12500))
        MAF.value(0)
        MAR.value(1)
        MBF.value(1)
        MBR.value(0)
        ReadSensors()
        if IR_Values[0] == 0 and IR_Values[1] == 0 and IR_Values[2] == 0 and IR_Values[3] == 0 and IR_Values[4] == 0 and IR_Values[5] == 0 and IR_Values[6] == 0:
            flag = 1
    while flag == 1:
        Stop()
        while IR_Values[3] == 0:
            MAC.duty_u16((19500))
            MBC.duty_u16((19500))
            MAF.value(0)
            MAR.value(0)
            MBF.value(1)
            MBR.value(0)
            IR_Values[3] = IR_Sensors[3].value()
        flag = 2  
    Stop()
    Mode = 0
    
def Stop():
    MAF.value(0)
    MAR.value(0)
    MBF.value(0)
    MBR.value(0)
    
def Extramove():
    MAC.duty_u16(19500)
    MBC.duty_u16(19500)
    MAF.value(1)
    MAR.value(0)
    MBF.value(1)
    MBR.value(0)
    sleep(0.4)
    Stop()
    
    
    
    
#loop
while True:
    r = 0
    while SB.value() == 0:
        kpT = str(kp)
        kiT = str(ki)
        kdT = str(kd)
        oled.text("kp=", 0, 0)
        oled.text(kpT, 25, 0)
        oled.text("ki=", 0, 10)
        oled.text(kiT, 25, 10)
        oled.text("kd=", 0, 20)
        oled.text(kdT,25, 20)
        oled.show()
        oled.fill(0)
    sleep(1)
    if CB.value() == 1:
        sys.exit()
    while CB.value() == 0:
        LinePosition()
        print("MODE",Mode)
        while Mode == 0:
            LinePosition()
            PIDControl()
            MAC.duty_u16((MAV))
            MBC.duty_u16((MBV))
            MAF.value(1)
            MAR.value(0)
            MBF.value(1)
            MBR.value(0)
        while Mode == 1:
            #LinePosition()
            LeftTurn()
            break
        while Mode == 2:
            #LinePosition()
            IR_Values[3] = IR_Sensors[3].value()
            if IR_Values[3] == 1:
                Mode = 1
            RightTurn()
            break
        while Mode == 3:
            Extramove()
            IR_Values[2] = IR_Sensors[2].value()
            IR_Values[3] = IR_Sensors[3].value()
            IR_Values[4] = IR_Sensors[4].value()
            while IR_Values[2] == 1 or IR_Values[3] == 1 or IR_Values[4] == 1:
                Mode = 1
                break
            BackTurn()
            break
        while Mode == 4:
            CrossTurn()
            break
        while Mode == 5:
            YCross()
            break
        while Mode == 6:
            AcuteLeft()
            break
        while Mode == 7:
            AcuteRight()
            break
        
        
        















