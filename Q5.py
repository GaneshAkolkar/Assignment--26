import threading

total_sum = 0

def add_values(start, end):
    global total_sum
    for i in range(start, end + 1):
        total_sum += i

thread1 = threading.Thread(target=add_values, args=(1, 50))
thread2 = threading.Thread(target=add_values, args=(51, 100))

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Total Sum:", total_sum)
