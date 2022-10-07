x = int(input("Digite um número impar: "))
i = -1
if x%2 == 0:
    print("NÚMERO ÍMPAR BURRÃO!")
while i <= x:
    i += 1
    if i%2 == 1:
        print(i)
