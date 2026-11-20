# mylist = [1, 2, 3, 4, 5, 6]
#
# for i in mylist:
#     total = 0
#     if i % 2 != 0:
#         total += i
#     else:
#         continue
#
# print(total)
#
#
#
# tesyt
#
# test(replace("Mississippi", "i" , "I"), "MIssIsIppI")
#
# s = "I love spom! Spom is my favorite food. Spom, spom, spom, yum!"
# test(replace(s, "om", "am"),
#      "I love spam! Spam is my favorite food. Spam, spam, spam, yum!")
#
# test(replace(s, "o", "a"),
#      "I lave spam! Spam is my favarite faad. Spam, spam, spam, yum!")


import sys


def test(actual, expected):
    """Beklenen değer ile gerçek değeri karşılaştırır ve sonucu yazdırır."""
    line_num = sys._getframe(1).f_lineno
    if actual == expected:
        msg = f"{line_num}. satırdaki test BAŞARILI."
    else:
        msg = (
            f"{line_num}. satırdaki test BAŞARISIZ: "
            f"beklenen '{expected}', gelen '{actual}'."
        )
    print(msg)


def replace(s, old, new):
    """s metnindeki tüm old ifadelerini new ile değiştirir."""
    return new.join(s.split(old))


test(replace("Mississippi", "i", "I"), "MIssIsIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, spom, yum!"
test(
    replace(s, "om", "am"),
    "I love spam! Spam is my favorite food. Spam, spam, spam, yum!",
)

test(
    replace(s, "o", "a"),
    "I lave spam! Spam is my favarite faad. Spam, spam, spam, yum!",
)