n = int(input("Digite um termo: "))
i = 0
x = 0
s = 0
termo = '''1
-
{}'''

while i < n:
    x += 2
    i += 1
    s += x
    print("\n" + termo.format(x))
print("\nSoma:", s)
