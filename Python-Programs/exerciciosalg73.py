r=int(input("Digite as maneiras: "))
n=int(input("Digite os objetos: "))
def fatorial(x):
    i=1
    n=2
    while i<x:
        i+=1
        n=n*i
    return i
c=fatorial(n)/fatorial(r)*fatorial((n-r))
print("Maneiras: ",c)
