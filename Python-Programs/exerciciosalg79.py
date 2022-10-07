n=int(input("Digite quantas strings você quer ver as estastíticas: "))
i=0
# def howMuchwords(x):
#     i=0
#     s=-1
#     x=str(x)
#     while i<=len(x):
#         s+=1
#         ns=''
#         if x[s]!='\x20':
#         i+=1
while i<n:
    s=str(input("Digite a {}ª strings: ".format(i+1)))
    if s.isalnum() == True: 
        print("String:", s, "é alfanúmerica.")
    else:
        print("String:", s, "não é alfanúmerica.")
    if s.isalpha() == True:
        print("String:", s, "é alfabetica.")
    else:
        print("String:", s, "não é alfabetica.")
    print("Caracteres digitados:", len(s))
    print("Palavras digitadas:", s.count('\x20')+1)
    
    i+=1