import threading
import time

exitFlag = 0
duration1 = time.time()

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter, delay):
        threading.Thread.__init__(self)

        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.delay = delay

    def run(self):
        print("Starting " + self.name)
        print(self)
        print_time(self.name, self.counter, self.delay)
        print("Exiting " + self.name)

def print_time(threadName, counter, delay):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s %d" % (threadName, time.ctime(time.time()),counter))
        print(threading.active_count())
        counter -= 1
                
# Create new threads
thread1 = myThread(1, "Thread-1", 10, 1)
thread2 = myThread(2, "Thread-2", 5, 2)
thread3 = myThread(3, "Thread-3", 3, 3)
thread4 = myThread(4, "Thread-4", 7, 4)
thread5 = myThread(5, "Thread-5", 2, 5)

# Start new Threads
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()

duration2 = time.time()
execution_time = duration2 - duration1

print("Exiting Main Thread")
print(f"The execution time is: {execution_time}")