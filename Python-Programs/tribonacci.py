x=int(input("Digite o um termo para ver sequencia de tribonacci: "))
i=0
a=1
b=1 
c=2
while i<x:
    t=a+b+c
    a=b # 1, 2, 4
    b=c # 2, 4, 7
    c=t # 4, 7, 13
    print(a)
    i+=1
