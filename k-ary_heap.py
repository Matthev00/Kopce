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


def extract_max(arr, n, k):
    max_elem = arr[0]
    arr[0] = arr[n - 1]
    n -= 1
    restore_down(arr, n, 0, k)
    return max_elem


def draw_heap(arr, k):
    height = math.ceil(math.log(len(arr), k))
    level = 0
    element = 0
    elements_in_level = 1
    while element < len(arr):
        helper = (k**(height-level))
        sys.stdout.write("  " * (helper//2))
        for i in range(elements_in_level):
            if element + i >= len(arr):
                break
            sys.stdout.write(f"{arr[level+i]}")
            sys.stdout.write(" "*(helper+(height-level)**k))
        print()
        element += elements_in_level
        level += 1
        elements_in_level *= k


arr = [4, 5, 6, 7, 8, 9, 10, 7, 9, 150, 75, 11]
k = 7

build_heap(arr, len(arr), k)
print("Built Heap:")
print(arr[:len(arr)])

elem = 3
insert(arr, len(arr), k, elem)
print("\nHeap after insertion of", elem, ":")
print(arr[:len(arr)])

max_elem = extract_max(arr, len(arr), k)
print("\nExtracted max is", max_elem)
print("Heap after extract max:")
print(arr[:len(arr)])

draw_heap(arr, k)