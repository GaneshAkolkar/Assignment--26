import threading
import time

def print_current_time():
    while True:
        current_time = time.strftime("%H:%M:%S")
        print(f"Current Time: {current_time}")
        time.sleep(1)

def print_minute_completed():
    while True:
        print("1 Minute Completed")
        time.sleep(60)

thread1 = threading.Thread(target=print_current_time)
thread2 = threading.Thread(target=print_minute_completed)

thread1.start()
thread2.start()
