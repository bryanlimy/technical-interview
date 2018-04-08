from timeit import default_timer as timer
from numpy.random import randint

def all_subset_sum(S, t, result, partial=[]):
    """ Returns all possible combinations of subset sum"""
    if sum(partial) == t:
        result.append(partial)
    elif sum(partial) < t:
        for i in range(len(S)):
            all_subset_sum(S[:i] + S[i+1:], t, result, partial + [S[i]])


def subset_sum1(S, t):
    """ Return True if there is a possible subset sum"""
    if t in S:
        return True
    else:
        for i in range(len(S)):
            if subset_sum1(S[i+1:], t - S[i]):
                return True
    return False


def subset_sum2(S, t):
    if not S:
        return False
    elif t in S:
        return True
    else:
        return subset_sum2(S[1:], t) or subset_sum2(S[1:], t - S[0])


def subset_sum_dp(S, t, i, memo=dict()):
    # key = "%d:%d" % (t, S[0])
    # if key in memo:
    #     return memo[key]
    # elif not S:
    #     return False
    # elif t == 0:
    #     return True
    # elif t < 0:
    #     return False
    # else:
    #     memo[key] = subset_sum_dp(S[1:], t, memo) or subset_sum_dp(S[1:], t - S[0], memo)
    # return memo[key]
    key = "%d:%d" % (t, i)
    if key in memo:
        return memo[key]
    if t == 0:
        return True
    elif t < 0:
        return False
    else:
        memo[key] = subset_sum_dp(S, t - S[i], i - 1, memo) or \
                    subset_sum_dp(S, t, i - 1, memo)
    return memo[key]


if __name__ == "__main__":
    S = list(randint(100, size=100, dtype=int))
    #S = [2, 4, 6, 10]
    t = 256
    # result = []
    # start = timer()
    # all_subset_sum(S, t, result, [])
    # end = timer()
    # print("all subsets sum %s time (ms) %.4f\n" % (str(result), (end - start) * 1000))

    start = timer()
    result = subset_sum1(S, t)
    end = timer()
    print("Subset sum 1 result %s time (ms) %.4f" % (str(result), (end - start) * 1000))

    start = timer()
    result = subset_sum2(S, t)
    end = timer()
    print("Subset sum 2 result %s time (ms) %.4f" % (str(result), (end -start) * 1000))

    memo = dict()
    start = timer()
    result = subset_sum_dp(S, t, len(S) - 1, memo)
    end = timer()
    print("Subset sum DP result %s time (ms) %.4f" % (str(result), (end -start) * 1000))
