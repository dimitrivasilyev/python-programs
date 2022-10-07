# Deslocate to right <---
m=int(input("Digite um número de deslocamento: "))
#n=int(input("Digite o tamanho do vetor: "))
v=[-3,7,11,0,8]
print(v)
for i in range(0,m):
    v+=[v.pop(0)]
print(v)
