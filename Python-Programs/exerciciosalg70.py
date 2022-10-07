x = int(input("Digite sua idade: "))
print("Calculando a soma até o termo da sua idade...\n")
n = 0
i = 0
s = 0
while i < x:
    i += 1
    n += 1
    print(n)
    s += n
print("\nSoma até o termo {}: {}".format(x, s))
