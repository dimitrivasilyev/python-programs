import time

n=int(input("Digite um número e veja se ele é perfeito: "))
s=0
i=0
while i<n:
    i+=1
    time.sleep(0.5)
    print(i)
    s+=i
    if s==n:
        print("Número",s,"é perfeito")
        quit()
print("Número não é perfeito")
