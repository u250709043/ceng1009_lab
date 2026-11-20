def sum_of_squares(xs):
    toplam = 0
    for x in xs:
        toplam += x ** 2
    return toplam

print(sum_of_squares([2, 3, 4]))

