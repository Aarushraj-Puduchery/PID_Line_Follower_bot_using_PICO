from machine import Pin,PWM,I2C
from utime import sleep,sleep_ms
import ssd1306
#Button
UB=Pin(13,Pin.IN,Pin.PULL_DOWN)
LB=Pin(12,Pin.IN,Pin.PULL_DOWN)
DB=Pin(11,Pin.IN,Pin.PULL_DOWN)
RB=Pin(10,Pin.IN,Pin.PULL_DOWN)
CB=Pin(4,Pin.IN,Pin.PULL_DOWN)
BB=Pin(5,Pin.IN,Pin.PULL_DOWN)
#IRSensors
IRL=Pin(26,Pin.IN)
IR0=Pin(16,Pin.IN)
IR1=Pin(17,Pin.IN)
IR2=Pin(18,Pin.IN)
IR3=Pin(19,Pin.IN)
IR4=Pin(20,Pin.IN)
IR5=Pin(21,Pin.IN)
IR6=Pin(22,Pin.IN)
IRR=Pin(27,Pin.IN)
IRLV=0
IR0V=0
IR1V=0
IR2V=0
IR3V=0
IR4V=0
IR5V=0
IR6V=0
IRRV=0
IR_Sensors2cm=[IRL,IR0,IR1,IR2,IR3,IR4,IR5,IR6,IRR]
IR_Values2cm=[IRLV,IR0V,IR1V,IR2V,IR3V,IR4V,IR5V,IR6V,IRRV]
IR_Sensors3cm=[IRL,IR0,IR1,IR3,IR5,IR6,IRR]
IR_Values3cm=[IRLV,IR0V,IR1V,IR2V,IR3V,IR4V,IRRV]

i2c = I2C(0, sda=Pin(0), scl=Pin(1))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)
count = 0
count2 = 0
count3 = 0
Power1 = 0
Mode = 0
# Kp = 0
# Ki = 0
# Kd = 0

def ReadSensors2cm():
    for i in range(0,9):
        if i==0 or i==8:
            IR_Values2cm[i] = int(not (IR_Sensors2cm[i].value()))
            continue
        IR_Values2cm[i] = IR_Sensors2cm[i].value()
    sleep(0.01)

def ReadSensors3cm():
    for i in range(0,7):
        if i==0 or i==6:
            IR_Values3cm[i] = int(not (IR_Sensors3cm[i].value()))
            continue
        IR_Values3cm[i] = IR_Sensors3cm[i].value()
    sleep(0.01)
    
def LinePositionDispfor2cm():
    ReadSensors2cm()
    for i in range(0,9):
        if IR_Values2cm[i] == 1:
            oled.fill_rect(i*15, 10, 10, 16, 1)
            oled.show()
        if IR_Values2cm[i] == 0:
            oled.text("_", (i*15), 16)
            oled.show()
            
def LinePositionDispfor3cm():
    ReadSensors3cm()
    for i in range(0,7):
        if IR_Values3cm[i] == 1:
            oled.fill_rect(i*15, 10, 10, 16, 1)
            oled.show()
        if IR_Values3cm[i] == 0:
            oled.text("_", (i*15), 16)
            oled.show()
    
while True:
    if UB.value() == 1:
        count = count - 1
    if DB.value() == 1:
        count = count + 1
    #print(count)
    sleep(0.15)
    
    if count >= 3:
        count = 3
    if count < 0:
        count = 0
        
    if count == 0:
        oled.text("1 Start", 0, 0)
        oled.show()
        oled.fill(0)
    elif count == 1:
        oled.text("2 Edit", 0, 0)
        oled.show()
        oled.fill(0)
    elif count == 2:
        oled.text("3 Mode", 0, 0)
        oled.show()
        oled.fill(0)
    elif count == 3:
        oled.text("4 Setting", 0, 0)
        oled.show()
        oled.fill(0)
        
    #Start
    if count == 0 and CB.value() == 1:
        while True:
            if Mode == 0 and CB.value() == 1:
                oled.text("PID_LF_2cm", 0, 0)
                oled.show()
                oled.fill(0)
                sleep(1)
                while True:
                    LinePositionDispfor2cm()
                    sleep_ms(10)
                    oled.fill(0)
                    if CB.value() == 1:
                        oled.show()
                        oled.fill(0)
                        break
                with open("PID_LF_2cm.py") as Code2cm:
                    exec(Code2cm.read())
                #run one
            if Mode == 1 and CB.value() == 1:
                oled.text("PID_LF_3cm", 0, 0)
                oled.show()
                oled.fill(0)
                sleep(1)
                while True:
                    LinePositionDispfor3cm()
                    sleep_ms(10)
                    oled.fill(0)
                    if CB.value() == 1:
                        oled.show()
                        oled.fill(0)
                        break
                with open("PID_LF_3cm.py") as Code3cm:
                    exec(Code3cm.read())
                #run two
            if BB.value() == 1:
                break
            
    #Edit    
    if count == 1 and CB.value() == 1:
        while True:
            if UB.value() == 1:
                count2 = count2 - 1
            if DB.value() == 1:
                count2 = count2 + 1
            #print(count)
            sleep(0.15)
            
            if count2 >= 2:
                count2 = 2
            if count2 < 0:
                count2 = 0
                
            if count2 == 0:
                oled.text("Kp value", 0, 0)
                oled.show()
                oled.fill(0)
            elif count2 == 1:
                oled.text("Ki value", 0, 0)
                oled.show()
                oled.fill(0)
            elif count2 == 2:
                oled.text("Kd value", 0, 0)
                oled.show()
                oled.fill(0)
            if BB.value() == 1:
                break
            #Kp Value
            if count2 == 0 and CB.value() == 1:
                while True:
                    if UB.value() == 1:
                        Power1 = Power1 - 1
                    if DB.value() == 1:
                        Power1 = Power1 + 1
                    #print(count)
                    sleep(0.15)
                    if Power1> 3:
                        Power1 = 3
                    if Power1 < -4:
                        Power1 = -4
                    if Power1 == 0:
                        oled.text("1", 0, 20)
                        oled.show()
                        #oled.fill(0)
                    elif Power1 == 1:
                        oled.text("10", 0, 20)
                        oled.show()
                        #oled.fill(0)
                    elif Power1 == 2:
                        oled.text("100", 0, 20)
                        oled.show()
                        #oled.fill(0)
                    elif Power1 == 3:
                        oled.text("1000", 0, 20)
                        oled.show()
                    elif Power1 == -1:
                        oled.text("0.1", 0, 20)
                        oled.show()
                    elif Power1 == -2:
                        oled.text("0.01", 0, 20)
                        oled.show()
                    elif Power1 == -3:
                        oled.text("0.001", 0, 20)
                        oled.show()
                    elif Power1 == -4:
                        oled.text("0.0001", 0, 20)
                        oled.show()
                    KpFile=open("KpValue.csv","r")
                    Kp = float(KpFile.read())
                    KpText = str(Kp)
                    oled.text(KpText, 0, 0)
                    oled.show()
                    oled.fill(0)
                    KpFile.close()
                    if LB.value() == 1:
                        Kp = (Kp - (1*pow(10,Power1)))
                        KpFile=open("KpValue.csv","r+")
                        KpFile.seek(0)
                        KpText = str(Kp)
                        KpFile.write(KpText)
                        #KpFile.truncate()
                        KpFile.close()
                        oled.text(KpText, 0, 0)
                        oled.show()
                        oled.fill(0)
                        sleep(0.15)
                    if RB.value() == 1:
                        Kp = (Kp + (1*pow(10,Power1)))
                        KpFile=open("KpValue.csv","r+")
                        KpFile.seek(0)
                        KpText = str(Kp)
                        KpFile.write(KpText)
                        #KpFile.truncate()
                        KpFile.close()
                        oled.text(KpText, 0, 0)
                        oled.show()
                        oled.fill(0)
                        sleep(0.15)
                    if CB.value() == 1:
                        Kp=0
                        KpFile=open("KpValue.csv","r+")
                        KpFile.seek(0)
                        KpText = str(Kp)
                        KpFile.write(KpText)
                        #KpFile.truncate()
                        KpFile.close()
                        oled.text(KpText, 0, 0)
                        oled.show()
                        oled.fill(0)
                        sleep(0.15)
                    if BB.value() == 1:
                        break
            #Ki Value
            if count2 == 1 and CB.value() == 1:
                 while True:
                    if UB.value() == 1:
                        Power1 = Power1 - 1
                    if DB.value() == 1:
                        Power1 = Power1 + 1
                    #print(count)
                    sleep(0.15)
                    if Power1> 3:
                        Power1 = 3
                    if Power1 < -4:
                        Power1 = -4
                    if Power1 == 0:
                        oled.text("1", 0, 20)
                        oled.show()
                        #oled.fill(0)
                    elif Power1 == 1:
                        oled.text("10", 0, 20)
                        oled.show()
                        #oled.fill(0)
                    elif Power1 == 2:
                        oled.text("100", 0, 20)
                        oled.show()
                        #oled.fill(0)
                    elif Power1 == 3:
                        oled.text("1000", 0, 20)
                        oled.show()
                    elif Power1 == -1:
                        oled.text("0.1", 0, 20)
                        oled.show()
                    elif Power1 == -2:
                        oled.text("0.01", 0, 20)
                        oled.show()
                    elif Power1 == -3:
                        oled.text("0.001", 0, 20)
                        oled.show()
                    elif Power1 == -4:
                        oled.text("0.0001", 0, 20)
                        oled.show()
                    KiFile=open("KiValue.csv","r")
                    Ki = float(KiFile.read())
                    KiText = str(Ki)
                    oled.text(KiText, 0, 0)
                    oled.show()
                    oled.fill(0)
                    KiFile.close()
                    if LB.value() == 1:
                        Ki = (Ki - (1*pow(10,Power1)))
                        KiFile=open("KiValue.csv","r+")
                        KiFile.seek(0)
                        KiText = str(Ki)
                        KiFile.write(KiText)
                        KiFile.close()
                        oled.text(KiText, 0, 0)
                        oled.show()
                        oled.fill(0)
                        sleep(0.15)
                    if RB.value() == 1:
                        Ki = (Ki + (1*pow(10,Power1)))
                        KiFile=open("KiValue.csv","r+")
                        KiFile.seek(0)
                        KiText = str(Ki)
                        KiFile.write(KiText)
                        KiFile.close()
                        oled.text(KiText, 0, 0)
                        oled.show()
                        oled.fill(0)
                        sleep(0.15)
                    if CB.value() == 1:
                        Ki = 0
                        KiFile=open("KiValue.csv","r+")
                        KiFile.seek(0)
                        KiText = str(Ki)
                        KiFile.write(KiText)
                        KiFile.close()
                        oled.text(KiText, 0, 0)
                        oled.show()
                        oled.fill(0)
                        sleep(0.15)
                    if BB.value() == 1:
                        break
            #Kd Value
            if count2 == 2 and CB.value() == 1:
                 while True:
                    if UB.value() == 1:
                        Power1 = Power1 - 1
                    if DB.value() == 1:
                        Power1 = Power1 + 1
                    sleep(0.15)
                    if Power1> 3:
                        Power1 = 3
                    if Power1 < -4:
                        Power1 = -4
                    if Power1 == 0:
                        oled.text("1", 0, 20)
                        oled.show()
                    elif Power1 == 1:
                        oled.text("10", 0, 20)
                        oled.show()
                    elif Power1 == 2:
                        oled.text("100", 0, 20)
                        oled.show()
                    elif Power1 == 3:
                        oled.text("1000", 0, 20)
                        oled.show()
                    elif Power1 == -1:
                        oled.text("0.1", 0, 20)
                        oled.show()
                    elif Power1 == -2:
                        oled.text("0.01", 0, 20)
                        oled.show()
                    elif Power1 == -3:
                        oled.text("0.001", 0, 20)
                        oled.show()
                    elif Power1 == -4:
                        oled.text("0.0001", 0, 20)
                        oled.show()
                    KdFile=open("KdValue.csv","r")
                    Kd = float(KdFile.read())
                    KdText = str(Kd)
                    oled.text(KdText, 0, 0)
                    oled.show()
                    oled.fill(0)
                    KdFile.close()
                    if LB.value() == 1:
                        Kd = (Kd - (1*pow(10,Power1)))
                        KdFile=open("KdValue.csv","r+")
                        KdFile.seek(0)
                        KdText = str(Kd)
                        KdFile.write(KdText)
                        KdFile.close()
                        oled.text(KdText, 0, 0)
                        oled.show()
                        oled.fill(0)
                        sleep(0.15)
                    if RB.value() == 1:
                        Kd = (Kd + (1*pow(10,Power1)))
                        KdFile=open("KdValue.csv","r+")
                        KdFile.seek(0)
                        KdText = str(Kd)
                        KdFile.write(KdText)
                        KdFile.close()
                        oled.text(KdText, 0, 0)
                        oled.show()
                        oled.fill(0)
                        sleep(0.15)
                    if CB.value() == 1:
                        Kd = 0
                        KdFile=open("KdValue.csv","r+")
                        KdFile.seek(0)
                        KdText = str(Kd)
                        KdFile.write(KdText)
                        KdFile.close()
                        oled.text(KdText, 0, 0)
                        oled.show()
                        oled.fill(0)
                        sleep(0.15)
                    if BB.value() == 1:
                        break
    #Mode     
    if count == 2 and CB.value() == 1:
        while True:
            if UB.value() == 1:
                count3 = count3 - 1
            if DB.value() == 1:
                count3 = count3 + 1
            #print(count)
            sleep(0.15)
            
            if count3 > 3:
                count3 = 3
            if count3 < 0:
                count3 = 0
                
            if count3 == 0:
                oled.text("PID LF 2cm", 0, 0)
                oled.show()
                oled.fill(0)
                Mode = 0
            elif count3 == 1:
                oled.text("PID LF 3cm", 0, 0)
                oled.show()
                oled.fill(0)
                Mode = 1
            elif count3 == 2:
                oled.text("Other", 0, 0)
                oled.show()
                oled.fill(0)
            if BB.value() == 1:
                break
    
    if count == 3 and CB.value() == 1:
        while True:
            if UB.value() == 1:
                count4 = count4 - 1
            if DB.value() == 1:
                count4 = count4 + 1
            #print(count)
            sleep(0.15)
            
            if count4 > 3:
                count4 = 3
            if count4 < 0:
                count4 = 0
                
            if count4 == 0:
                oled.text("Speed", 0, 0)
                oled.show()
                oled.fill(0)
            elif count4 == 1:
                oled.text("other", 0, 0)
                oled.show()
                oled.fill(0)
            elif count4 == 2:
                oled.text("Other", 0, 0)
                oled.show()
                oled.fill(0)
            if BB.value() == 1:
                break



