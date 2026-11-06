import turtle


def drawBar(t, height, label):
    """
    Tek bir barı ve üstündeki etiketi çizen fonksiyon.
    Etiketin barın üst çizgisiyle çakışmaması için yukarı taşıma payı bırakılmıştır.
    """
    # Barın dolgu rengini ve kenar çizgisini ayarlayalım
    t.begin_fill()

    # Barın çizimi (sol alt köşeden başlayarak)
    t.left(90)
    t.forward(height)

    # --- İstenen Ekstra Geliştirme: Etiketi barın tamamen üzerine yazdırmak ---
    # Dolguyu bozmadan veya çizgiyle çakıştırmadan önce küçük bir boşluk bırakıyoruz
    up_distance = 15  # Etiketin barın ne kadar üstünde duracağı (piksel cinsinden)

    t.penup()
    t.forward(up_distance)  # Barın tepesinden biraz daha yukarı çık
    t.write(f"  {height} ({label})", align="center", font=("Arial", 10, "normal"))
    t.backward(up_distance)  # Tekrar barın tepesine geri dön
    t.pendown()
    # ------------------------------------------------------------------------

    t.right(90)
    t.forward(40)  # Barın genişliği
    t.right(90)
    t.forward(height)
    t.left(90)

    t.end_fill()

    # Barlar arasında boşluk bırakmak için sağa dönüp biraz ilerleyelim
    t.penup()
    t.forward(10)  # Barlar arası boşluk
    t.pendown()


def barChart(t, data):
    """
    Sayısal listeyi alarak tüm barları çizen non-fruitful ana fonksiyon.
    """
    for val in data:
        drawBar(t, val, str(val))


# --- Ana Program (Main Program) ---
# Turtle ekranı ve kaplumbağa nesnesini hazırlayalım
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("white")

t = turtle.Turtle()
t.color("blue")
t.fillcolor("lightblue")
t.pensize(2)
t.speed(5)

# Çizimin ekranın sol alt köşesinden düzgün başlaması için konumlandıralım
t.penup()
t.goto(-250, -150)
t.pendown()

# Örnek veri listemiz (bar yükseklikleri)
data = [48, 117, 200, 240, 160, 260, 220]

# barChart fonksiyonunu çağırarak grafiği çizdirelim
barChart(t, data)

# Pencerenin açık kalmasını sağla
turtle.done()