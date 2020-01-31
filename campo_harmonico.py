notas = ['Dó','Dó#','Ré','Ré#','Mi','Fá','Fá#','Sol','Sol#','Lá','Lá#','Si']
entrada = input().split()
M = [2,2,1,2,2,2,1]
m = [2,1,2,2,1,2,2]
lista = [M,m]
start = notas.index(entrada[0])
dic = {'M':0,'m':1}
tom = dic[entrada[1]]
def faz_escala(start):
    escala = []
    cont = 0
    while True:
        escala.append(notas[start])
        try:
            start+= lista[tom][cont]
            if start > 11 :
                start = (start - 11) - 1
            cont += 1
        except:
            break
    return escala
print(faz_escala(start))
