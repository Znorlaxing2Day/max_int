n = int(input("Enter the length of the sequence: ")) # Do not change this line
teljari = 1
a = 1
b = 2
c = 3
d = a + b + c

while teljari < n + 1:
    if teljari == 1:
        print(a)
    elif teljari == 2:
        print(b)
    elif teljari == 3:
        print(c)
    elif teljari == 4:
        print(d)
    else:
        a = b
        b = c
        c = d
        d = a + b + c 
        print(d)
    teljari += 1