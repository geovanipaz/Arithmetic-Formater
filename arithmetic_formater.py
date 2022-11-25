
def arithmetic_arranger(array, resultado=False):
    cont = 0
    s1 = []
    s2 = []
    s3 = []
    linha = []
    l= []
    while cont < len(array):
        temp = array[cont].split(' ')
        l.append(temp)
        cont +=1
    c = 0
    while c < len(l):
        s2.append(l[c][1]+ l[c][2].rjust(4,' '))
        linha.append('-----')
        r1 = int(l[c][0])
        r2 = int(l[c][2])
        if l[c][1] == '+':
            temp3 = str(r1+r2).rjust(5,' ')
            s3.append(temp3)
        elif l[c][1] == '-':
            temp3 = str(r1-r2).rjust(5,' ')
            s3.append(temp3)
        c+=1
    ss1 = "    ".join(s1)
    ss2 = "    ".join(s2)
    ssl = "    ".join(linha)
    ss3 = "    ".join(s3)
    print(ss1)
    print(ss2)
    print(ssl)
    if resultado:
        print(ss3)
    
        
        
a = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49","23 - 123","32 - 8"]   
arithmetic_arranger(a, True)