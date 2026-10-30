# 1 den n e kadar toplanacak
#
#
# bi kendisi yapsın
#
# bi de hespa makinesiyle n * (n+1) ile


def hesapla(s,e):
    i = 0
    for j in range(s,e+1):
        i = i + j

    return i


print(hesapla(1,10))

