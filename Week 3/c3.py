import threading
from threading import Lock
from threading import Thread
import time

cv = threading.Condition()
control = 1


def func1():
    global control
    while True:
        if control == 1:
            cv.acquire()
            time.sleep(0.3)
            print ("Thread: ",control)
            control = 2
            cv.notifyAll()
            cv.release()

def func2():
    global control
    while True:
        if control == 2:
            cv.acquire()
            time.sleep(0.3)
            print ("Thread: ",control)
            control = 3
            cv.notifyAll()
            cv.release()

def func3():
    global control
    while True:
        if control == 3:
            cv.acquire()
            time.sleep(0.3)
            print ("Thread: ",control)
            control = 4
            cv.notifyAll()
            cv.release()

def func4():
    global control
    while True:
        if control == 4:
            cv.acquire()
            time.sleep(0.3)
            print("Thread: ",control)
            control = 0
            cv.notifyAll()
            cv.release()

t1 = Thread(target=func1,args=())
t2 = Thread(target=func2,args=())
t3 = Thread(target=func3,args=())
t4 = Thread(target=func4,args=())
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()



