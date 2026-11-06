import math

def findHypot(a, b):
    """Given the lengths of two sides of a right-angled triangle, 
    returns the length of the hypotenuse.
    """
    return (a ** 2 + b ** 2) ** 0.5

    # Alternatively using math.sqrt:
    # return math.sqrt(a ** 2 + b ** 2)

# Example usage:
print(findHypot(3, 4))  # Output: 5.0