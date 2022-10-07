n=int(input("Digite o tamanho do vetor: "))
x=[]
s=0
for i in range(1, n+1):
    x.append(i)
for nums in x:
    if nums%2==0:
        s+=nums
print("Vetor:",x)
print("Soma dos números pares:\033[1;32m",s)
