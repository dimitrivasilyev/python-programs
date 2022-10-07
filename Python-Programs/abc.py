a=int(input("Digite o valor de A: "))
b=int(input("Digite o valor de B: "))
c=int(input("Digite o valor de C: "))
if a>b:
    if b>c:
        print(a,b,c)
    elif a>c:
        print(a,c,b)
    print(c,a,b)
elif b>c:
    if a>c:
        print(b,a,c)
    else:
        print(b,c,a)
else:
    print(c,b,a)
