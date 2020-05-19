from time import sleep
import threading
import time
import concurrent.futures
import random

def p1 (name):
    global x
    print('\nПисатель '+str(name) +' стартовал.')
    lock.acquire()
    local = x
    print('Пишет..')
    x = local * 2
    lock.release()
    print('Писатель ' + str(name) + ' закончил писать.\n')
    time.sleep(5) # Спим

class Readers:

    def __call__(self, rep=10, sleep_time=0.5):
        global c
        c = random.randint(1, 5)
        for i in range(c):
            m = random.randint(1, 15)
            print('Читатель %s читает в данный момент' % m)
            sleep(sleep_time)


if __name__ == '__main__':
    b = Readers()
    for z in range(3):
        print ('\nНовый цикл')
        x = 1
        lock = threading.Lock()
        for i in range(1,3):
            l = threading.Thread(target=p1, args=(i,))
            l.start()
            t2 = threading.Thread(target=b, args=(3,))
            t2.start()
            t2.join()

        l.join()