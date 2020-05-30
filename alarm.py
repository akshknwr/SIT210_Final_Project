#! /usr/bin/env python3
import RPi.GPIO as GPIO
from time import sleep
#Disable warnings 
GPIO.setwarnings(False)
#Select GPIO mode
GPIO.setmode(GPIO.BCM)
#Set buzzer - pin 23 as output
buzzer=4
alarmStatus=False
GPIO.setup(buzzer,GPIO.OUT)



def triggerAlarm(duration):
    alarmStatus = True
    writeFile('true')
    
    try:
         while True:
              fin = open("status.txt", "rt")
              if(fin.read() == "true"):
                  GPIO.output(buzzer, GPIO.HIGH)
                  sleep(duration)
                  GPIO.output(buzzer, GPIO.LOW)
                  sleep(duration) 
                      
    except KeyboardInterrupt:
        print("Interrupt occured")
        writeFile('false')
        GPIO.output(buzzer, GPIO.LOW)
	

	

def startAlarm(alarmType):
    duration=0
    if(alarmType=="flood"):
        duration=0.2
    triggerAlarm(duration)
    
def writeFile(content):
    fout =open('status.txt','wt')
    fout.write(content)
    fout.close()
    
    
def stopAlarm():
    GPIO.output(buzzer,GPIO.LOW)
    alarmStatus=False
    writeFile('false')
    GPIO.cleanup()
def getAlarmStatus():
    return alarmStatus
startAlarm("flood")
