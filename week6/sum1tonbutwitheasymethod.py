# e * (e+1) / 2
from itertools import count


def sum(s,e):
    for s in range(s,e+1):
         deger = (e * (e+1) / 2) - ((s-1) * s / 2) # bölme işleminde float çıkarttık
        return deger


print(sum(5,10))




# çok çok küçük bir boşluk şu hatayı görmene sebep oluyor File "/home/student/ceng1009_lab/week6/sum1tonbutwitheasymethod.py", line 8
#     return deger
#                 ^
# IndentationError: unindent does not match any outer indentation level
#
# bu deger in yanındaki ^ işaretidiyor ki satırı doğru atmamışsın satırsal hata var diyor