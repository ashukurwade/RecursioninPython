def sum(n):
    if n <= 1:   # base case
        return n
    else:        # general or recursive case
        ans = sum(n - 1)
    return n + ans


print(sum(6))
