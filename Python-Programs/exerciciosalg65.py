n = int(input("Digite um número e veja sua fatorial: "))
i = 2
y = 1
x = 1
t = 0
while i <= n:
    y = y*i
    i += 1
    x += 1
while t < n:
    t += 1
    print(t, end='') 
print("\nResultado:",y)
