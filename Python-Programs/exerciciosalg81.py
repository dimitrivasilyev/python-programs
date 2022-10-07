#v 1.2 /*\- Add minutes in algorithm \*/
ih=int(input("Digite o inicio da palestra hora: "))
fh=int(input("Digite o final da palestra hora: "))
th=0
if ih>=24:
    print("[\33[1;31m-\033[0m]ERRO: Não é possivel calcular com horario acima de 24:00")
elif fh>=24:
    print("[\33[1;31m-\033[0m]ERRO: Não é possivel calcular com horario acima de 24:00")
else:
    if ih<=fh:
        while ih<=fh:
            ih+=1
            th+=1
            #for i in range(ih,fh):
            #    th=i
        print("A palestra deu:", th-1,"horas.")
    elif ih>=fh:
        while ih>=fh:
            ih+=1
            th+=1
            if ih==25:
                ih=0
        if ih==0:
            while ih<fh:
                ih+=1
                th+=1
            print(ih)
                #for i in range(fh,ih):
                #    th=i
        print("A palestra deu:", th-1,"horas.")

