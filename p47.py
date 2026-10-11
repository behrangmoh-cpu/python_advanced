import multiprocessing
def print_cube(num):
    print("Cube: {}".format(num * num * num))
    for i in range(100):
        print(f"cube = {i}")

def print_square(num):
    print("Square: {}".format(num * num))
    for i in range(100):
            print(f"squre = {i}")

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=print_square, args=(10, ))
    p2 = multiprocessing.Process(target=print_cube, args=(10, ))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("Done!")