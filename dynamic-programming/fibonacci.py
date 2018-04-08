from timeit import default_timer as timer

def fib_recursive(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_recursive_dp(n, memo=[]):
    if n == 1 or n == 2:
        return 1
    if memo[n] is None:
        memo[n] = fib_recursive_dp(n - 1, memo) + fib_recursive_dp(n - 2, memo)
    return memo[n]


def fib_bottom_up(n):
    memo = [None] * (n + 1)
    memo[1] = memo[2] = 1
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


def main():
    n = 20

    start = timer()
    result = fib_recursive(n)
    end = timer()
    print("%d-th fib recursive result %d time (ms) %.4f" % (n, result, (end - start) * 1000))

    start = timer()
    memo = [None] * (n + 1)
    result = fib_recursive_dp(n, memo)
    end = timer()
    print("%d-th fib recursive DP result %d time (ms) %.4f" % (n, result, (end - start) * 1000))

    start = timer()
    result = fib_bottom_up(n)
    end = timer()
    print("%d-th fib bottom up result %d time (ms) %.4f" % (n, result, (end - start) * 1000))


if __name__ == "__main__":
    main()