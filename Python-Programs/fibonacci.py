x=int(input("Digite o termo: "))
i=0
a=1
b=0
while i<x:
    t=a+b
    a=b
    b=t
    i+=1
    print(a)

