import turtle


def draw_bar(t, height):
    """Turtle t kullanarak verilen yükseklikte bir bar çizer.
       Negatif değerlerde yazıyı sıfır ekseninde, pozitiflerde tepesinde gösterir.
    """
    t.begin_fill()  # Barı doldurmaya başla
    t.left(90)

    if height < 0:
        # Negatif değerler için: Yazıyı sıfır ekseninde yaz, sonra aşağı doğru çiz
        t.write("  " + str(height))
        t.forward(height)  # Eksenin altına doğru in
        t.right(90)
        t.forward(40)  # Barın genişliği
        t.right(90)
        t.forward(-height)  # Şekli kapatmak için yukarı çık
        t.left(90)
    else:
        # Pozitif veya sıfır değerler için: Yukarı çık, yazıyı tepesine yaz
        t.forward(height)  # Yukarı çık
        t.write("  " + str(height))  # Yazıyı tepeye yaz
        t.right(90)
        t.forward(40)  # Barın genişliği
        t.right(90)
        t.forward(height)  # Eksen tabanına geri dön
        t.left(90)

    t.end_fill()  # Dolguyu tamamla
    t.forward(10)  # Barlar arasında boşluk bırak


# Ekran ve kaplumbağa (turtle) ayarları
wn = turtle.Screen()
wn.bgcolor("lightgreen")

t = turtle.Turtle()
t.pensize(3)

# Hem pozitif, hem negatif, hem de farklı renk aralıklarını içeren test verileri
data = [48, 117, 200, -50, 240, -120, 160, 99, 222, 75]

# Başlangıç pozisyonu (Ekranın sol tarafı)
t.penup()
t.goto(-300, 0)  # Sıfır ekseni ortada daha rahat görünsün diye dikey konumu 0 yaptık
t.pendown()

for value in data:
    # Değere göre renk atama (if-elif-else)
    if value >= 200:
        t.color("red")
    elif value >= 100:
        t.color("yellow")
    else:
        t.color("green")

    draw_bar(t, value)

turtle.done()