t = int(input("Digite um termo: "))
i = 0
x = 1
s = 0

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

while i < t:
    x += 1
    if isCousin(x):
        i += 1
        s += x
        print(x)
if i == t:
    print("\nÚltimo número:",x)
print("Até o {}º termo, a soma é de: {}".format(t, s))
