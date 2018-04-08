from timeit import default_timer as timer


def all_subset_sum(S, t, result, partial=[]):
    """ Returns all possible combinations of subset sum"""
    if sum(partial) == t:
        result.append(partial)
    elif sum(partial) < t:
        for i in range(len(S)):
            all_subset_sum(S[:i] + S[i+1:], t, result, partial + [S[i]])


def subset_sum(S, t):
    """ Return True if there is a possible subset sum"""
    if t in S:
        return True
    else:
        for i in range(len(S)):
            if subset_sum(S[i+1:], t - S[i]):
                return True
    return False


if __name__ == "__main__":
    S = [1, 2, 3, 4, 5, 8, 10, 12]
    t = 12
    start = timer()
    result = subset_sum(S, t)
    end = timer()
    print("naive: " + str(result) + ", time: " + str(end - start) + "s")

    result = []
    start = timer()
    all_subset_sum(S, t, result, [])
    end = timer()
    print("all possible subset: " + str(result) + ", time: " + str(end - start) + "s")
