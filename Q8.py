import threading

def print_numbers():
    for i in range(1, 6):
        print(f"Thread Name: {threading.current_thread().name}, Number: {i}")

thread = threading.Thread(target=print_numbers, name="CustomThreadName")

thread.start()
thread.join()
