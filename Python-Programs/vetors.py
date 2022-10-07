q=[0,35,4,22,20,36,30]
print("Há",len(q)-1,"salas...")
sala=int(input("Digite a sala: "))
if (len(q)-len(q))+1>=1 and len(q)<=6:
    print("Sala não encontrada.")
else:
    print("Sala: "+str(sala))
    print(q[sala],"alunos...")
