import sys
import math


def restore_down(arr, length, index, k):
    child = [0] * (k + 1)
    while True:
        for i in range(1, k + 1):
            child[i] = k * index + i if k * index + i < length else -1

        max_child, max_child_index = -1, 0
        for i in range(1, k + 1):
            if child[i] != -1 and arr[child[i]] > max_child:
                max_child_index = child[i]
                max_child = arr[child[i]]

        if max_child == -1:
            break

        if arr[index] < arr[max_child_index]:
            arr[index], arr[max_child_index] = arr[max_child_index], arr[index]

        index = max_child_index


def restore_up(arr, index, k):
    parent = (index - 1) // k
    while parent >= 0:
        if arr[index] > arr[parent]:
            arr[index], arr[parent] = arr[parent], arr[index]
            index = parent
            parent = (index - 1) // k
        else:
            break


def build_heap(arr, n, k):
    for i in range((n - 1) // k, -1, -1):
        restore_down(arr, n, i, k)


def insert(arr, n, k, elem):
    arr.append(elem)
    n += 1
    restore_up(arr, n - 1, k)
    return n


def extract_max(arr, n, k):
    max_elem = arr[0]
    arr[0] = arr[n - 1]
    n -= 1
    restore_down(arr, n, 0, k)
    del arr[-1]
    return max_elem, n

def draw(arr, k, elements=1, pos=0, prev_max_pos=0, indent=""):
    if elements == 1:
        print(arr[0])
        elements = k
        pos = k
    for index in range(k):
        if (pos < len(arr)):
            print(indent, end="")
            print("|----", end="")
            print(arr[pos])
            if prev_max_pos + elements + k * (pos - prev_max_pos - 1) + 1 < len(arr):
                newpos = prev_max_pos + elements + k * (pos - prev_max_pos)
                if index != k - 1: draw(arr, k, elements*k, newpos, prev_max_pos + elements, indent + "|    ")
                else: draw(arr, k, elements*k, newpos, prev_max_pos + elements, indent + "     ")
        pos -= 1
    print(indent)

arr = [4, 5, 6, 7, 8, 9, 10]
k = 3
n = len(arr)

build_heap(arr, n, k)
print("Built Heap:")
print(arr)

elem = 3
n = insert(arr, n, k, elem)
print("\nHeap after insertion of", elem, ":")
print(arr)
draw(arr, k)

max_elem, n = extract_max(arr, n, k)
print("\nExtracted max is", max_elem)
print("Heap after extract max:")
print(arr)
draw(arr, k)

# # test draw for 2
# tst2 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# draw(tst2, 2)

# # test draw for 3
# tst3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# draw(tst3, 3)

# # test draw for 7
# tst7 = [x for x in range(61)]
# draw(tst7, 7)