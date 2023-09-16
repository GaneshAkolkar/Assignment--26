import threading
import random

random_numbers = []

def fill_list_with_random_numbers():
    for _ in range(20):
        random_numbers.append(random.randint(1, 100))

threads = []

for _ in range(5):
    t = threading.Thread(target=fill_list_with_random_numbers)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Random Numbers:", random_numbers)
