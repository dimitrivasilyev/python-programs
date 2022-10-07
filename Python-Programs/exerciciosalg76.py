# O algoritmo ele remove o ultimo caractere do valor inteiro
# e exibe o ultimo caractere: variavel 'ni' guarda o valor e depois
# guarda o mesmo valor sem o ultimo caractere
# variavel 'no' guarda o ultimo caractere da variavel 'ni'.
ni=int(input("Digite um valor inteiro: "))
no=0
pin=0
if pin<1:  
    pfr=ni%10
    no=no*10+pfr
    pin=ni//10
    ni=pin
print(ni)
print(no)
