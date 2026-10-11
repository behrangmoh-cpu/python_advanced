import threading

def worker():
    print("Thread is working...")
def leason():
    print("thread is python.......")
t = threading.Thread(target=worker)
t1= threading.Thread(target=leason)
print("Thread created but not started yet.")
t.start()
t1.start()
