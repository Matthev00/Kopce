import sys
import math


def restore_down(arr, length, index, k):
    child = [0] * (k + 1)
    while True:
        for i in range(1, k + 1):
            child[i] = k * index + i if k * index + i < length else -1 # uzupełniamy indeksami dzieci

        max_child, max_child_index = -1, 0
        for i in range(1, k + 1):
            if child[i] != -1 and arr[child[i]] > max_child: #szukamy największego dziecka
                max_child_index = child[i]
                max_child = arr[child[i]]

        if max_child == -1:
            break

        if arr[index] < arr[max_child_index]:
            arr[index], arr[max_child_index] = arr[max_child_index], arr[index] # zamiana, jeśli dziecko jest większe od rodzica

        index = max_child_index # sprawdzamy dla podmienionego dziecka


def restore_up(arr, index, k): # rodzic zamienia się z dzieckiem
    parent = (index - 1) // k
    while parent >= 0:
        if arr[index] > arr[parent]:
            arr[index], arr[parent] = arr[parent], arr[index]
            index = parent
            parent = (index - 1) // k
        else:
            break


def build_heap(arr, k):
    heap = [arr[-1]]
    n=1
    for element in reversed(arr[:-1]):
        n = insert(heap, n, k, element)
    return heap
    

def insert(arr, n, k, elem):
    arr.append(elem)
    n += 1
    restore_up(arr, n - 1, k)
    return n


def extract_max(arr, n, k):
    max_elem = arr[0]
    arr[0] = arr[n - 1] #podstawienie ostatniego elementu w korzeń 
    n -= 1
    restore_down(arr, n, 0, k) #naprawa
    del arr[-1]
    return max_elem, n

def draw(arr, k, pos=0, indent=""):
    if pos == 0:
        print(arr[0])
        pos = k
    for index in range(k):
        if (pos < len(arr)):
            print(indent, end="")
            print("|----", end="")
            print(arr[pos])
            if k*pos + 1 < len(arr):
                newpos = k * (pos + 1)
                if index != k - 1: draw(arr, k, newpos, indent + "|    ")
                else: draw(arr, k, newpos, indent + "     ")
        pos -= 1
    print(indent)

# arr = [4, 5, 6, 7, 8, 9, 10]
# k = 3
# n = len(arr)

# build_heap(arr, n, k)
# print("Built Heap:")
# print(arr)

# elem = 3
# n = insert(arr, n, k, elem)
# print("\nHeap after insertion of", elem, ":")
# print(arr)
# draw(arr, k)

# max_elem, n = extract_max(arr, n, k)
# print("\nExtracted max is", max_elem)
# print("Heap after extract max:")
# print(arr)
# draw(arr, k)

if __name__ == "__main__":
    # arr = [50, 10, 15, 50, 40, 40, 100]
    # build_heap(arr, len(arr), 2)
    # print(arr)
    # test draw for 2
    tst2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    # tst2 = build_heap(tst2, 2)
    draw(tst2, 2)

    # test draw for 5
    tst5 = [i for i in range(34)]
    # tst5 = build_heap(tst5, 5)
    draw(tst5, 5)

    # test draw for 7
    tst7 = [x for x in range(61)]
    #tst7 = build_heap(tst7, 7)
    draw(tst7, 7)