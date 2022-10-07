a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
print("\n[\33[1;33m*\033[0m]Verificando se os três valores digitados correspondem a um de triângulo...")
if a < b + c and b < a + c and c < a + b:
    print("\n[\33[1;32m+\033[0m]Valores digitados correspondem a um triângulo.")
else:
    print("\n[\33[1;31m-\033[0m]Valores não correspondem a de um triângulo.")
