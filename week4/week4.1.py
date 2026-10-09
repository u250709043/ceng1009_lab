import turtle
#
# kenar = int(input("Kenar sayısını girin: "))
# renk = input("Rengi girin: ")
# kenaruzunluk = int(input("Kenar uzunluğunu girin: "))
# acı = int(input("2 kenar arasındaki açıyı girin: "))
#
ok = turtle.Turtle()
#
#
#
# for i in range(kenar):
#     for i in [renk]:
#         ok.color(i)
#         ok.forward(kenaruzunluk)
#         ok.left(acı)

# for i in range(1,101, 1):
#     print("We like Python's turtles!")
#
#
#

#
# for i in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
#     print(f"One of the months of the year is {i}")

#
# for i in [ 12, 10, 32, 3, 66, 17, 42, 99, 20]:
#     print(i)
#     print(i**2)





ok.penup()
ok.goto(-200,0)
ok.pendown()

for i in range(4):
    ok.forward(10)
    ok.left(90)

ok.penup()
ok.goto(-100, 0)
ok.pendown()
for i in range(3):
    ok.forward(10)
    ok.left(120)

ok.penup()
ok.goto(0, 0)
ok.pendown()

for i in range(8):
    ok.forward(10)
    ok.left(45)





for i in range(8):
    ok.forward(10)
    ok.left(45)