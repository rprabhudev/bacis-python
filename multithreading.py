#multi threading
from time import sleep # to use sleep function
from threading import * #to use multi threading

class Good(Thread):
    def run(self):
        for i in range(5):
            print("good")
            sleep(1) # sleep  the thread or 1 second
class Morning(Thread):
    def run(self):
        for i in range(5):
            print("morning")
            sleep(1)

t1 = Good()
t2 = Morning()

t1.start()# start the thread
sleep(.2)
t2.start()

t1.join()#after the completion of thread join to main thread 
t2.join()

print("bye")