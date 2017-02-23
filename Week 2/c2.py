from threading import Lock
from threading import Thread
import threading
import time
import random

lines = []
pos = 0
#lock = Lock()
cv = threading.Condition()

with open("caged_bird.txt","r") as file:
    lines = [line.strip() for line in file]

def printValue(val):
    print (val,"\n")
  

def readLines1():
    #lock.acquire()
    for x in range(0,len(lines)):
        global pos
        if x >= len(lines)-1:
            print ("GOT HERE")
            x = 0
        print (x)
        pos = x
        #print (pos)
        time.sleep(.3)
    #lock.release()

def readLines2():
    #lock.acquire()
    for y in range(0, len(lines)):
        global pos
        if y >= len(lines)-1:
            y = 0
        #print (pos)
        print (lines[pos])
        time.sleep(.3)
    #lock.release()

def conVar():
    access = input("Enter: ")
    cv.acquire()
    if (access==2):
        print ("I can do a thing")
        secs = random.randint(10,14)
        print (secs)
        time.sleep(secs)
        cv.notifyAll()
        cv.release()
        access=3
    else:
        cv.notifyAll()
        cv.release()

def noMenu():
    t3 = Thread(target=readLines1,args=())
    t4 = Thread(target=readLines2,args=())
    t5 = Thread(target=conVar,args=())
    t3.start()
    t4.start()
    t5.start()
    t3.join()
    t4.join()
    t5.join()
def menu(): 
    print("Please enter which thread you would like to start: \na) Thread 1\nb) Thread 2\nc) Thread 1 & 2\nd) Exit")
    answer = input("Enter: ")
    if answer == "a":
        t3 = Thread(target=readLines1,args=())
        t3.start()
        t3.join()
    elif answer == "b":
        print ("test")
        t4 = Thread(target=readLines2,args=())
        t4.start
        t4.join
    elif answer == "c":
        t3 = Thread(target=readLines1,args=())
        t4 = Thread(target=readLines2,args=())
        t3.start()
        t4.start()
        t3.join()
        t4.join()
    elif answer == "d":
        exit()
    else:
        "Please enter a valid input!"
        menu()
    menu()
noMenu()

#t1 = Thread(target=printValue,args=(1,))
#t2 = Thread(target=printValue,args=(1,))