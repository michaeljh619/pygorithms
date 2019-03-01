def naive(n):
    # base case
    if n <= 1:
        return n

    # recursive case
    return naive(n-2) + naive(n-1)


def dynamic(n):
    # create fibonacci list
    fib = [0, 1]
    i = 2
    while i <= n:
        next_num = fib[i-2] + fib[i-1]
        fib.append(next_num)
        i += 1

    return fib[n]
