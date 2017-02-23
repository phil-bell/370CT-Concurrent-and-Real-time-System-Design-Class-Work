from threading import Thread
import time

lines = []
global pos

with open("caged_bird.txt","r") as file:
    lines = [line.strip() for line in file]

def printValue(val):
    print (val,"\n")
  

def readLines1():
    for x in range(0,len(lines)):
        pos = x
        print (lines[pos])
        time.sleep(.3)

def readLines2():
    for y in range(0, len(lines)):
        pos = y
        print (lines[pos])
        time.sleep(.3)

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
menu()

#t1 = Thread(target=printValue,args=(1,))
#t2 = Thread(target=printValue,args=(1,))