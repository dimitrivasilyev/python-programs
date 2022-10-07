n = int(input("Digite quantas valores você quer ver o maior entre eles: "))
i = 0
while i < n:
    i += 1
    x = int(input("Digite o {}º número: ".format(i)))
    maior = x
    if x > maior:
        maior = x
print("Maior número:", maior)
