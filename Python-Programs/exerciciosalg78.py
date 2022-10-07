s=str(input("Digite uma palavra: "))
ns=''
i=0
while i<len(s):
    if s[i] != ' ':
        ns+=s[i]
    i+=1
print(ns)
