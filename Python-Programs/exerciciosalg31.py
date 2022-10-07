import math

vo = int(input("Digite o valor de Vo: "))
teta = int(input("Digite o valor de θ: "))
g = 9.8
teta = teta*3.14/180
S = (vo**2)*math.sin(2*teta)/g
print("Alcance do projétil:",S)
