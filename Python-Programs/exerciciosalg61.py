x = int(input("Digite um número: "))
par = 2
impar = 1
i = 1
while i <= 50:
    impar += 2
    calc = 2*impar/x+impar
    i += 1
print("Resultado:",calc)
