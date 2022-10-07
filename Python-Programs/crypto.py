#/bin/python3
import sys
if len(sys.argv)>=3 or len(sys.argv)==1:
    print("python3 temp.py {string}")
    quit()
string=sys.argv[1]
n=len(sys.argv)
class Alg:
    def code(s):
        alg=['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII', 'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI', 'XXXII', 'XXXII', 'XXXIV', 'XXXV', 'XXXVI']
        strings=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' , 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        ns=''
        x=-1
        x_verification=0
        x_str=0
        i=0
        String=s
        if len(s)>=len(alg)+1:
            print("\33[1;31m[ERRO]\033[0mString deve ser menor que 26 caracteres.")
            quit()
        try:
            while i<=len(String):
                if String[x_verification]==x:
                    if strings[x]==String[x_str]:
                        getpos=alg[strings.index(strings[x])] 
                        ns+=getpos
                        x_str+=1
                        i+=1
                    else:
                        x+=1
                    x_verification+=1
                if strings[x]==String[x_str]:
                    getpos=alg[strings.index(strings[x])] 
                    ns+=getpos
                    x_str+=1
                    i+=1
                else:
                    x+=1
        except IndexError:
            print(ns)
    def decode(s):
        print(s)
Alg.code(string)
Alg.decode(string)
