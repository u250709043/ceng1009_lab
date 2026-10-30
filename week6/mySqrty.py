def mySqrt(n):
    oldguess = n / 2

    while True:
        newguess = 0.5 * (oldguess + n/oldguess)
        if abs(newguess - oldguess) < 0.00001:
            return newguess

        oldguess = newguess


print(mySqrt(25))
print(mySqrt(100))
