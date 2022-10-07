n = int(input("Quantos termos deseja calcular a soma dos quadrados: "))
i = 0
calc = 0 
while i < n:
    i += 1
    x = int(input("Digite o {}º valor: ".format(i)))
    calc += x**2
print("Resultado:",calc)
