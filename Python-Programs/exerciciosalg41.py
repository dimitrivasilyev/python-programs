x = int(input("Digite um número par: "))
i = 0
if x%2 == 1:
    print("NÚMERO PAR PORRA!")
while i <= x:
    i += 1
    if i%2 == 0:
        print(i)
