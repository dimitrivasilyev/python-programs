acum=int(input("Digite o primeiro operando: "))
op=str(input("Digite a operação aritmética: "))
if op=='=':
    print(acum)
else:           # Trying to recreate a case decision estructure.
    val=int(input("Digite o segundo operando: "))
    # CASE
    if op=='+':# '+'
        print("Resultado:", acum+val)
    elif op=='-': # '-'
        print("Resultado:", acum-val)
    elif op=='*': # '*'
        print("Resultado:", acum*val)
    elif op=='/': # '/'
        print("Resultado:", acum/val)
    else:
        print("\33[1;31mERRO\033[0m: Operador desconhecido.")
