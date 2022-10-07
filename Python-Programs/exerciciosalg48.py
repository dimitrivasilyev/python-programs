n = int(input("Digite um número e veja se ele é triangular ou não: "))
i = 0
v = 0
while v < n:
    i += 1
    v = i*(i+1)*(i+2)
if v == n:
    print("Número é triangular.")
else:
    print("Número não é triangular.")
