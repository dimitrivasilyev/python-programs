d = int(input("Digite o valor do diâmetro: "))
q = int(input("Digite a o valor da carga: "))
if d > 100:
    n = 2
elif d < 50:
    n = 6
else:
    n = 4
s = (4*q/3.14)*(d**2)*n
print("A tensão:",s)
