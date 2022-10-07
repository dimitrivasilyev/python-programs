r = int(input("Digite um número: "))
n = int(input("Digite uma quantidade de objetos: "))

def fatorial(x):
    i = 1
    n = 1
    while i <= x:
        n = n*i
        i += 1
    return n
c = fatorial(n)/fatorial(r)*fatorial((n-r))
print("Maneiras possíveis:",c)
