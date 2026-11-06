import turtle

t = turtle.Turtle()
t.speed(5)


def draw_n_pointed_star(t, n, length):
    # n'in tek sayı ve 3'ten büyük/eşit olduğunu kontrol edelim
    if n < 3 or n % 2 == 0:
        print("Hata: n tek bir sayı ve en az 3 olmalıdır!")
        return

    # Yıldızın kaç derece döneceğini hesaplıyoruz
    # n köşeli yıldız için dış açı formülü
    angle = 180 - (180 / n)
    # Alternatif (daha dik/keskin yıldızlar için): angle = 180 - (360 / n) * 2 gibi de ayarlanabilir.
    # Ancak standart düzgün yıldız poligonu için:

    # Doğru düzgün yıldız çizimi için atlama faktörü (skip) hesaplanır:
    # Genellikle n köşeli yıldızda her adımda (n // 2) adım ileri atlanır.
    skip = n // 2

    for _ in range(n):
        t.forward(length)
        t.right(180 - (180 * skip / n))  # veya standart açı formülü


# Daha sade ve garanti çalışan Turtle yıldız algoritması:
def star(t, n, length):
    if n < 3 or n % 2 == 0:
        print("n 3 veya daha büyük bir tek sayı olmalıdır!")
        return

    # Her bir köşe için dönme açısı
    angle = 180 - (180 / n)  # veya 360 * k / n mantığı

    # Alternatif net çalışan döngü:
    for _ in range(n):
        t.forward(length)
        t.left(360 * (n // 2) / n)  # Yıldızın iç hatlarını oluşturan atlamalı dönüş


# Test edelim (Örn: 7 köşeli yıldız, kenar uzunluğu 100)
star(t, 11, 100)

turtle.done()