import time
from threading import Thread

def func1():
    print('Starting function 1')
    time.sleep(2)
    print('Finished function 1')

def func2():
    print('Starting function 2')
    time.sleep(2)
    print('Finished function 2')

#func1()
#func2()

t1 = Thread(target=func1)
t1.start()

t2 = Thread(target=func2)
t2.start()
