x = int(input("Digite o primeiro valor: "))
y = int(input("Digite o segundo valor: "))
print('\n')
if x < y:
    while x <= y:
        print(y) 
        y -= 1
    print('\r')
elif y < x:
    while y <= x:
        print(x)
        x -= 1
    print('\r')
else:
    exit()
