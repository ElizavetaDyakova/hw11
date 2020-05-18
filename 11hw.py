# Есть два писателя, которые по очереди в течении определенного времени (у каждого разное) пишут в одну книгу.
# Данная книга очень популярна, у неё есть как минимум 3 фаната (читателя), которые ждут не дождутся,
# чтобы прочитать новые записи из неё. Каждый читатель и писатель – отдельный поток.
# Одновременно книгу может читать несколько читателей, но писать единовременно может только один писатель.


#Решение 1, не уверена, что правильно
#решила добавить больше читателей
import threading
import os
from time import sleep
import random


#Создаем класс первого писателя
class Writers:
    def __call__(self, count=1, sleep_time=0.5, first=1):
        for i in range(count):
            print('Писатель %s пишет' % first)
            sleep(sleep_time)
            print('Писатель %s закончил писать' % first)
            sleep(sleep_time)


#создаем класс второго писателя
class Writers2:
    def __call__(self, count=1, sleep_time=2, num=2):
        for i in range(count):
            sleep(sleep_time)
            print('Писатель %s пишет' % num)
            sleep(sleep_time)
            print('Писатель %s закончил писать' % num)
            # sleep(sleep_time)


#создаем класс читателей
class Readers:
    def __call__(self, rep=10, count=15, sleep_time=0.5):
        for i in range(count):
            m = random.randint(1, 15)
            print('Читатель %s читает в данный момент' % m)
            sleep(sleep_time)




if __name__ == '__main__':
    a = Writers()
    c = Writers2()
    b = Readers()
    #потоки
    t1 = threading.Thread(target=a, kwargs={'sleep_time': 1})
    t3 = threading.Thread(target=c, kwargs={'sleep_time': 4})
    t2 = threading.Thread(target=b, args=(12,))
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()


#Решение 2

class Writers:
    def __call__(self, count=1, sleep_time=0.5, first=1, sec=2):
        for i in range(count):
            print('Писатель %s пишет' % first)
            sleep(2)
            print('Писатель %s закончил писать' % first)
            sleep(sleep_time)
            print('Писатель %s пишет' % sec)
            sleep(5)
            print('Писатель %s закончил писать' % sec)
            sleep(sleep_time)





class Readers:
    def __call__(self, count=10, sleep_time=0.5):
        for i in range(count):
            m = random.randint(1, 10)
            print('Читатель %s читает в данный момент' % m)
            sleep(sleep_time)



if __name__ == '__main__':
    a = Writers()
    b = Readers()
    t1 = threading.Thread(target=a, kwargs={'sleep_time': 0.2})
    t2 = threading.Thread(target=b, args=(12,))
    t1.start()
    t2.start()

    t1.join()
    t2.join()