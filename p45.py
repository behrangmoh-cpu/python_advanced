import threading
def print_numbers():
 for i in range(20):
        print(f"number: {i}")
def print_numbers2():
    for i in range(100,110):
        print(f"number outer is {i}")
t = threading.Thread(target=print_numbers)
t1=threading.Thread(target=print_numbers2)
t.start()
t1.start()
t1.join()
