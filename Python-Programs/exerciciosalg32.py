a = int(input("Digite o lado a do triângulo: "))
b = int(input("Digite o lado b do triângulo: "))
c = int(input("Digite o lado c do triângulo: "))
s = (a+b+c)/2
k = s*(s-a)*(s-b)*(s-c)**0.5
print("Resultado:", k)
