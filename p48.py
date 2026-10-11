import multiprocessing
result = []

def square_list(mylist):
    #global result
    for num in mylist:
        result.append(num * num)

    print(f"Result(in process p1): {result}")
if __name__ == "__main__":
    list1 = [1, 2, 3, 4]

    p1 = multiprocessing.Process(target=square_list, args=(list1,))
    p1.start()
    p1.join()
    print(list1)
    print(f"Result(in main program): {result}")