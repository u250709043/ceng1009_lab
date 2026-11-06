def sumTo(n):
    accumulator = 0
    for i in range(1,n+1):
        accumulator += i
        if i != n:
            continue

        elif i == n:
            return accumulator



print(sumTo(5))