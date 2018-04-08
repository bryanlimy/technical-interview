def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    result = []
    i = 0
    j = 0
    while len(result) < len(left) + len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

        if i == len(left):
            result += right[j:]
            break
        if j == len(right):
            result += left[i:]
            break
    return result


def merge_sort(lst):
    if len(lst) < 2:
        return lst

    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])

    return merge(left, right)
