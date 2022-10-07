t = int(input("Digite o termo: "))
i = 0
a = 1
b = 0
while i < t:
    i += 1
    a, b = b, a
    a = a+b
    print(a)
