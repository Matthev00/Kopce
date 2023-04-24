import heap
import random
import matplotlib.pyplot as plt
import time
import gc


N = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000] # noqa 5501


def plot_create_time(heap_2, heap_5, heap_7, title):
    plt.plot(N, heap_2, color='r', label="2-ary heap") # noqa 5501
    plt.plot(N, heap_5, color='g', label="5-ary heap") # noqa 5501
    plt.plot(N, heap_7, color='b', label="7-ary heap") # noqa 5501
    plt.xlabel("Number of elements")
    plt.ylabel("Time in sec")
    plt.title(title)
    plt.legend()
    plt.savefig(title + '.png')
    plt.close()


def create_heap_time_measure(arr, k):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    heap.build_heap(arr, len(arr), k)
    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


def remove_time_measuer(arr, n, k):
    gc_old = gc.isenabled()
    gc.disable()
    start = time.process_time()
    id = len(arr)
    for _ in range(n):
        mel, id = heap.extract_max(arr, id, k)
    stop = time.process_time()
    if gc_old:
        gc.enable()
    return stop - start


def main():
    random_list = random.sample(range(1, 300000), 100000)
    n = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000] # noqa 5501
    heap_2_ary = random_list
    heap_5_ary = random_list
    heap_7_ary = random_list
    heap_2_ary_create_time = []
    heap_5_ary_create_time = []
    heap_7_ary_create_time = []
    heap_2_ary_remove_time = []
    heap_5_ary_remove_time = []
    heap_7_ary_remove_time = []
    heap.build_heap(heap_2_ary, 2, len(heap_2_ary))
    heap.build_heap(heap_5_ary, 5, len(heap_5_ary))
    heap.build_heap(heap_7_ary, 7, len(heap_7_ary))
    for number in n:
        heap_2_ary_create_time.append(create_heap_time_measure(heap_2_ary[:number], 2)) # noqa 5501
        heap_5_ary_create_time.append(create_heap_time_measure(heap_5_ary[:number], 5)) # noqa 5501
        heap_7_ary_create_time.append(create_heap_time_measure(heap_7_ary[:number], 7)) # noqa 5501
        heap_2_ary_remove_time.append(remove_time_measuer(heap_2_ary.copy(), number, 2)) # noqa 5501
        heap_5_ary_remove_time.append(remove_time_measuer(heap_5_ary.copy(), number, 5)) # noqa 5501
        heap_7_ary_remove_time.append(remove_time_measuer(heap_7_ary.copy(), number, 7)) # noqa 5501
    plot_create_time(heap_2_ary_create_time, heap_5_ary_create_time, heap_7_ary_create_time, "Building heaps") # noqa 5501
    plot_create_time(heap_2_ary_remove_time, heap_5_ary_remove_time, heap_7_ary_remove_time, "Remove") # noqa 5501


if __name__ == '__main__':
    main()
