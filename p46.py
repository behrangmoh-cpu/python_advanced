import threading
import time

def square(num):
    print(f"Square: {num*num}")
    for i in range(10):
        print(f"ss={i}")
    time.sleep(10)
    print(222222222222)

def cube(num):
    print(f"Cube: {num*num*num}")
    for i in range(10):
            print(f"cc={i}")
    time.sleep(2)
    print(11111111)

t1 = threading.Thread(target=square, args=(4,))
t2 = threading.Thread(target=cube, args=(4,))

t1.start()
t2.start()
t1.join()
t2.join()

print("Done!")