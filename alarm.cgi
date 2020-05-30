#! /usr/bin/env python3
print("Content-type: text/html\n\n");


import cgi

#fout=open('status.txt','wt')
alarmStatus=open("status.txt","rt")

form =cgi.FieldStorage()
alarmType = form.getvalue("alarm_type")



def stopAlarm():
    readAlarm=open("status.txt","rt")
    if(readAlarm.read()=="false"):
        print("Alarm is Already Stopped")
    else:
        alarmFile=open("status.txt","wt")
        alarmFile.write("false")
        alarmFile.close()
        print("Alarm is successfully Stopped")
    readAlarm.close()

#trigers alarm for certain testing period
def testAlarm():
    trigerAlarm()
    readAlarm=open("status.txt","rt")
    readstatus=readAlarm.read()
    
    
    #check if the test has worked
    if(readstatus=="true"):
        sleep(0.03) #test it for 3 seconds
        stopAlarm()
        print("alarm is tested and it is working")
    else:
        print("An error occurred") 
    

# trigers alarm indifinitely until manually stopped    
def trigerAlarm():
    alarmFile=open("status.txt","wt")
    alarmFile.write("true")
    alarmFile.close()
    print("Alarm is triggered")
    



if(alarmType=="stop"):
    stopAlarm()
elif(alarmType=="test"):
    testAlarm()
elif(alarmType=="trigger"):
    triggerAlarm()
    

