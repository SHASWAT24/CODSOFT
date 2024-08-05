import random
import string
def passwordgen(no):
    no = int(no)
    a = string.ascii_letters
    b = string.digits
    c = string.punctuation
    l = []
    l.extend(a)
    l.extend(b)
    l.extend(c)
    random.shuffle(l)
    g = "".join(l[0:no])
    return g

h=int(input("Enter the password length: "))
p=passwordgen(h)
print("YOUR GENERATED PASSWORD :",p)
