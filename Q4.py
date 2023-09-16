import threading

def print_even_numbers():
    for i in range(2, 101, 2):
        print(f"Even: {i}")

def print_odd_numbers():
    for i in range(1, 101, 2):
        print(f"Odd: {i}")

t1 = threading.Thread(target=print_even_numbers)
t2 = threading.Thread(target=print_odd_numbers)

t1.start()
t2.start()

t1.join()
t2.join()
