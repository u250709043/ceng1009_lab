import turtle

# Ekranı ve kaplumbağayı (tarihsel adıyla turtle) hazırlayalım
t = turtle.Turtle()
t.speed(5)  # Çizim hızı

# 1. Köşelere eklenecek süs fonksiyonu (drawSprite)
def drawSprite(t):
    # Süsün bacaklarını ve uçlarına minik üçgenleri çiziyoruz
    for _ in range(2):
        t.forward(15)     # Bacak uzunluğu
        # Uçlarına küçük bir üçgen ekleyelim:
        t.left(120)
        t.forward(5)
        t.left(120)
        t.forward(5)
        t.left(120)
        # Geri dönüp diğer bacağa geçiş
        t.backward(15)
        t.right(90)

# 2. Süslü kareyi çizen ana fonksiyon (fancySquare)
def fancySquare(t, uzunluk):
    for _ in range(4):
        t.forward(uzunluk)  # Karenin bir kenarı
        drawSprite(t)       # Köşeye gelince süsü çiz
        t.left(90)          # Bir sonraki kenar için 90 derece dön

# Çizimi başlatmak için fonksiyonu çağırıyoruz (Kenar uzunluğu: 150 birim)
fancySquare(t, 150)

# Pencerenin kapanmaması için tıklama bekletme
turtle.done()