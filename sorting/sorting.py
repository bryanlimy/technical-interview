from timeit import default_timer as timer
import numpy as np
from merge_sort import merge_sort
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from quick_sort import quick_sort


def main():
    sample = list(np.random.randint(1000, size=2000))
    target = sorted(sample)

    start = timer()
    bubble = bubble_sort(sample.copy())
    end = timer()
    assert bubble == target
    print("bubble sort time (ms) %.4f" % ((end - start) * 1000))

    start = timer()
    selection = selection_sort(sample.copy())
    end = timer()
    assert selection == target
    print("selection sort time (ms) %.4f" % ((end - start) * 1000))

    start = timer()
    merge = merge_sort(sample.copy())
    end = timer()
    assert merge == target
    print("merge sort time (ms) %.4f" % ((end - start) * 1000))

    start = timer()
    quick = quick_sort(sample.copy(), 0, len(sample) - 1)
    end = timer()
    assert quick == target
    print("quick sort time (ms) %.4f" % ((end - start) * 1000))

if __name__ == "__main__":
    main()
