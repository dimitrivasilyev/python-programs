n = str(input("Digite um número inteiro de 4 dígitos: "))
p1 = n[0:2] 
p2 = n[2:4]
print("Fatiamento:", p1, p2)
print("n = a+b = c² = n")
s = int(p1)+int(p2)
print(n[0:2],"+", n[2:4],"=",s)
if s**2 == int(n):
    print("{}² == {}".format(s, s**2))
    print("Número possui essa propriedade.")
else:
    print("{}² == {}".format(s, s**2))
    print("Número não possui a mesma propriedade.")
