x = str(input("Digite um número e veja se ele é palíndromo: "))
x_len = len(x)
n = -1
m = 0
i = 0
count = 0

def isPalindrome(x):
    n = 1
    count = 1
    len_x = len(str(x))
    if len_x%2 == 1:
        while n != len_x:
            n += 2
            count += 1
        return count
    else:
        print("Número não é palíndromo.")
        exit() 
while i <= x_len:
    n += 1
    m -= 1
    i += 1
    if x[n] == x[m]:
        count += 1
    else:
        print("Número não é palíndromo.")
        exit()
    if count == isPalindrome(x):
        print("Número é palíndromo.")
        exit()
