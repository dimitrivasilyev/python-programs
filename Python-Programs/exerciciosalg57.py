n = int(input("Digite um termo: "))
i = 1
s = 0

while i <= n:
    s += i
    print('\n',i)
    i += 1
print("\nA soma dos números até o termo", n, "foi", s)
