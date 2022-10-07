i = 1
x = 1
s = 0
t = 0

def isCousin(x):
    i = 0
    c = 0
    while i <= x or c < 2:
        i += 1
        if x%i == 0:
            c += 1
    if c <= 2:
        return True
    else:
        return False
try:
    while i < 2:
        x += 1
        if isCousin(x) == True:
            print(x)
            s += x
            t += 1
except KeyboardInterrupt:
    print("\a\nSoma: {} \nTermo: {}".format(s, t))
