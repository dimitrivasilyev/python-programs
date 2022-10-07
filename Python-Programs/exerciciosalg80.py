# v1.0
mensagem=str(input("Digite uma string: "))
busca=str(input("Digite um caractere que você deseja procurar na string que você acabou de digitar: "))
i=0
y=0
s=-1
n=0
print('\n'+mensagem)
print("Posição achada: ", end='')
# while y<len(mensagem):
#     y+=1
while i<len(mensagem):
    s+=1
    if mensagem[s]==busca:
        n+=s
        print(s,end=' ')
    i+=1
