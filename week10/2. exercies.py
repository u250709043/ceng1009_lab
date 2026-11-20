my_list = [76, 92.3, "hello", True, 4, 76]

# "apple" ve 76 değerlerini listenin sonuna ekle
my_list.append("apple")
my_list.append(76)

# 3. indekse "cat" değerini ekle
my_list.insert(3, "cat")

# Listenin başına 99 değerini ekle
my_list.insert(0, 99)

# "hello" değerinin indeksini bul
hello_index = my_list.index("hello")

# Listedeki 76 sayısının adedini say
count_76 = my_list.count(76)

# İlk 76 değerini listeden sil
my_list.remove(76)
my_list.remove(76)
my_list.remove(76)

# True değerini index ve pop kullanarak listeden çıkar
my_list.pop(my_list.index(True))

print(my_list)