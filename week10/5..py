def max(numbers):
    """Boş olmayan tam sayı listesindeki en büyük değeri döndürür."""
    largest = numbers[0]
    for num in numbers[1:]:
        if num > largest:
            largest = num
    return largest

print(max([3, 7, 2, 9, 5]))
print(max([-10, -3, -25, -1]))
print(max([42]))