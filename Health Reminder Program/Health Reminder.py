#  --------------------------------------------------------xx------------------------------------------------------------------------------------------------------------------
'''For Reference in Time'''
# times = ("9:30","9:45","10:00","10:30","11:00","11:15","11:30","12:00","12:30","12:45","1:00","1:30","2:00","2:15","2:30","3:00","3:30","3:45","4:00","4:30","5:00")
#            we      p      we     wep      we      p      we      wep     we      p       we     wep    we     p     we      wep    we     p      we    wep     we
# 10:30 12:00 1:30 3:00 4:30
#  9:45 11:15 12:45 2:15 3:45
# ---------------(Imports)-----------------------------------------xx------------------------------------------------------------------------------------------------------------------
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import time
import datetime
from pygame import mixer
#  ----------------(Functions)----------------------------------xx------------------------------------------------------------------------------------------------------------------
def getdate():
    localtime1 = time.asctime(time.localtime())
    return(localtime1)
def logins(act):
    f = open("logs.txt", "at")
    f.write(act)
    f.close()
    f = open("logs.txt", "at")
    f.write(" At Time: [ ")
    f.close()
    f = open("logs.txt", "at")
    f.write(str(getdate()))
    f.close()
    f = open("logs.txt", "at")
    f.write(" ]\n")
    f.close()
def readlog():
    f = open("logs.txt", "rt")
    print(f.read())
    f.close()

def physical():
    while True:
        mixer.init()
        mixer.music.load("physical.mp3")
        mixer.music.play(-1)
        time.sleep(2)
        a = input("\nPlease Do Any Exercise ,\nIn Order to Stop, Write 'Exdone' : ")
        a = a.capitalize()
        if a == "Exdone":
            mixer.music.stop()
            break
        else:
            time.sleep(1)
            continue
    logins("Physical Exercise Done")
def eyes():
    while True:
        mixer.init()
        mixer.music.load("eyes.mp3")
        mixer.music.play(-1)
        time.sleep(1)
        a = input("\nPlease Do Eye Exercise,\nIn Order to Stop, Write 'Eydone' : ")
        a = a.capitalize()
        if a == "Eydone":
            mixer.music.stop()
            break
        else:
            time.sleep(1)
            continue
    logins("Eye Exercise Done")
def water():
    while True:
        mixer.init()
        mixer.music.load("water.mp3")
        mixer.music.play(-1)
        time.sleep(1)
        a = input("\nPlease Drink Water,\nIn Order to Stop, Write 'Drank' : ")
        a = a.capitalize()
        if a == "Drank":
            mixer.music.stop()
            break
        else:
            time.sleep(1)
            continue
    logins("Water Drank")

def WaterandEyes():
    water()
    time.sleep(5)
    eyes()
def WaterEyesPhy():
    water()
    time.sleep(5)
    eyes()
    time.sleep(5)
    physical()

#  ------------(Main Program)-------------------------------------xx------------------------------------------------------------------------------------------------------------------

waterandeyeslist = [ "9:30" , "10:0", "11:0" , "11:30" , "12:30" , "13:0" , "14:0" , "14:30" , "15:30" , "16:0" , "17:0"]
watereyeandphylist = ["10:30" , "12:0" , "13:30" , "15:0" , "16:30"]
phylist = ["9:45" , "11:15" , "12:45" , "14:15" , "15:45"]


print("\nPlease Install pygames Module from 'cmd>>pip install pygames' Otherwise it will not Work\n")
time.sleep(2)
print("\nThis Program Will Make Sure You would Remain Fit While Using the Computer")
print("This Program will Only Run Between 9am to 5pm")
print("Please Follow All Instructions Carefully...")
time.sleep(10)
print("\nEvery 30 Minutes, You will be Reminded to Drink Water and Do Eye Exercise")
print("Every 45 Minutes, You will be Reminded to Do Any Kind of Physical Exercise")
print(" Starting Program .... \n")
time.sleep(10)
print("\nProgram Started!\n")
while True:
    now = datetime.datetime.now()
    currentt = (now.hour*3600) +(now.minute*60) +(now.second)
    curt=str(f"{now.hour}:{now.minute}")
    print(f"Present Time is : {curt}\n")
    time.sleep(2)
    if currentt in range(32400,61200):
        if curt in waterandeyeslist:
            WaterandEyes()
            time.sleep(60)
        elif curt in watereyeandphylist:
            WaterEyesPhy()
            time.sleep(60)
        elif curt in phylist:
            physical()
            time.sleep(60)
        elif curt == "9:00":
            time.sleep(60)
            continue
        else:
            print("\nThis is Working/Idle Time\n")
            time.sleep(2)
            print("\nWill Check For Reminder after 60 Seconds, Please Wait Patiently\n")
            time.sleep(56)
            continue
    else:
        print("\nWrong Time for the Program to Run, it can only work between 9am - 5pm \n")
        time.sleep(5)
        Reset = int((now.hour * 3600) + (now.minute * 60) + (now.second))
        Tleft= str(datetime.timedelta(seconds=((86400 + 32400) - Reset)))
        print("\nThe Program will Restart when it will be 9 am\n")
        time.sleep(5)
        print(f"\nApprox time left : {Tleft}")
        print(f"Program will Automatically Restart after {(86400 + 32400) - Reset } Seconds\n")
        time.sleep(8)
        query = str(input("Do You Want to See the Logs? To Do So type 'Logs' this will also Stop The Program,"
                          "Do You Want to Close the Program? If Yes then Type 'Quit' else Type anything to continue: "))
        query = query.capitalize()
        if query == "Quit":
            time.sleep(1)
            print("Terminated")
            break
        elif query == "Logs":
            time.sleep(3)
            print("\n")
            readlog()
            print("\n \n The Program will Stop in 15 Seconds")
            time.sleep(15)
            print("Terminated")
            break
        else:
            print("Wait Patiently, it may take a long time though...")
            time.sleep((86400 + 32400) - Reset)
            continue
