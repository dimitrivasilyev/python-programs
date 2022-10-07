n = int(input("Digite um número e veja se ele é primo ou não: "))
i = 0
count = 0
while i <= n or count < 2:
    i += 1
    if n%i == 0:
        count += 1
if count <= 2:
    print("Número é primo.")
else:
    print("Número não é primo.")
