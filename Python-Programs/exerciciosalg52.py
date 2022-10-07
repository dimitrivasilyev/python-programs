i = 1
s = 0
while i <= 30:
    x = int(input("Digite o {}º valor: ".format(i)))
    i += 1
    s += x
print("""\nSoma dos inversos:
1
-
{}""".format(s))
