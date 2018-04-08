def partition(lst, low, high):
    pivot = lst[high]
    i = low - 1
    for j in range(low, high):
        if lst[j] < pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1


def quick_sort(lst, low, high):
    if low < high:
        index = partition(lst, low, high)
        quick_sort(lst, low, index - 1)
        quick_sort(lst, index + 1, high)
    return lst
