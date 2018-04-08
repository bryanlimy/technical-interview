def partition(lst, low, high):
    # pick last element as pivot
    pivot = lst[high]
    # index of where pivot should be
    index = low
    for j in range(low, high):
        if lst[j] < pivot:
            lst[index], lst[j] = lst[j], lst[index]
            index += 1
    # place pivot at index
    lst[index], lst[high] = lst[high], lst[index]
    return index


def quick_sort(lst, low, high):
    if low < high:
        index = partition(lst, low, high)
        quick_sort(lst, low, index - 1)
        quick_sort(lst, index + 1, high)
    return lst
