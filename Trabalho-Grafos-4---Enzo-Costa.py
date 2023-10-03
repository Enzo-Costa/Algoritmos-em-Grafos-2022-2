from asyncio import Queue


def criaGrafoNormal():
    nomegrafo = input("digite o nome do grafo: ")
    tamgrafo = int(input("digite o numero de vertices do grafo: "))
    som = -1
    numeroarestas = 0
    controle = 0
    r = ""
    numerolacos = 0
    a = [[0 for x in range(tamgrafo)] for y in range(tamgrafo)]

    for c in range(tamgrafo):

            a[c][c] = 0
            for g in range(c + 1, tamgrafo):

                controle = 0
                while controle == 0:

                    r = input(f'Existe aresta ligando os vertices {c} e {g}? Digite s/n:')
                    if r == "s" or r == "S":
                        a[c][g] = 1
                        a[g][c] = 1
                        numeroarestas += 1
                        controle = 1

                    elif r == "n" or r == "N":
                        a[c][g] = 0
                        a[g][c] = 0
                        controle = 1

                    else:
                        print("Digite apenas S s / N n como resposta...")

    for i in range(tamgrafo):
                    print(a[i])
                    
    mats[numamts][0] = nomegrafo
    mats[numamts][1] = a
    

    with open(nomegrafo + '.txt', 'w+') as testfile:
        for row in a:
            testfile.write(' '.join([str(a) for a in row]) + '\n')
            
def criaCompleto():
    numvertices = int(input("Digite o numero de vertices do grafo: "))

    a = [[0 for x in range(numvertices)] for y in range(numvertices)]
    for c in range(0, numvertices):
        a[c][c] = 0
        for l in range(c + 1, numvertices):
            a[c][l] = 1
            a[l][c] = 1

    for i in range(numvertices):
        print(a[i])
        
    mats[numamts][0] = "Completo_" + str(numvertices)
    mats[numamts][1] = a
                
    with open("Completo_" + str(numvertices) + '.txt', 'w+') as testfile:
        for row in a:
            testfile.write(' '.join([str(a) for a in row]) + '\n')
            
def criaBipartido():
    n1 = int(input("Por favor digite o n1: "))
    n2 = int(input("Agora, por favor, digite o n2: "))

    a = [[0 for x in range(n1 + n2)] for y in range(n1 + n2)]

    for c in range(n1 + n2):
        for l in range(n1 + n2):
            if (c < n1 and l < n1) or (c >= n1 and l >= n1):
                a[c][l] = 0
            else:
                a[c][l] = 1

        for i in range(n1 + n2):
            print(a[i])
            
        mats[numamts][0] = "Bipartido_completo_" + str(n1) + "_" + str(n2)
        mats[numamts][1] = a

        with open("Bipartido_completo_" + str(n1) + "_" + str(n2) + '.txt', 'w+') as testfile:
            for row in a:
                testfile.write(' '.join([str(a) for a in row]) + '\n')

def criaEstrela():
    numvertices = int(input("Digite o numero de vertices do grafo: "))

    a = [[0 for x in range(numvertices)] for y in range(numvertices)]

    for c in range(numvertices):
        for l in range(numvertices):
            if (c == 0 or l == 0) and (c != l):
                a[c][l] = 1
            else:
                a[c][l] = 0

        for i in range(numvertices):
            print(a[i])
            
        mats[numamts][0] = "Estrela_" + str(numvertices)
        mats[numamts][1] = a

        with open("Estrela_" + str(numvertices) + '.txt', 'w+') as testfile:
            for row in a:
                testfile.write(' '.join([str(a) for a in row]) + '\n')
                
def criaCaminho():
    numvert = int(input("Digite o numero de vertices do grafo: "))
    
    a = [[0 for x in range(numvert)] for y in range(numvert)]
    
    cont = 0
    for i in range(0,int(numvert)-1):
        a[i][i+1] = 1
        a[i+1][i] = 1
        cont += 1

    for j in range (numvert):
        print(a[j])
        
    mats[numamts][0] = "Caminho_" + str(numvert)
    mats[numamts][1] = a

    print("O valor de |E|: " + str(cont))
    with open("Caminho_" + str(numvert) + '.txt', 'w+') as testfile:
            for row in a:
                testfile.write(' '.join([str(a) for a in row]) + '\n')
                
def criaCiclo():
    numvert = int(input("Digite o numero de vertices do grafo: "))
    
    a = [[0 for x in range(numvert)] for y in range(numvert)]
    
    cont = int(numvert)
    for i in range(0,numvert):
        a[i][(i+1)%numvert] = 1
        a[i][(i-1)%numvert] = 1
        
    a[0][numvert-1] = 1
    a[numvert-1][0] = 1
    
    for j in range (numvert):
        print(a[j])
    
    mats[numamts][0] = "Ciclo_" + str(numvert)
    mats[numamts][1] = a
        
    print("O valor de |E|: " + str(cont))
    with open("Ciclo_" + str(numvert) + '.txt', 'w+') as testfile:
            for row in a:
                testfile.write(' '.join([str(a) for a in row]) + '\n')
                
def criaRoda():
    numvert = int(input("Digite o numero de vertices do grafo: "))
    
    a = [[0 for x in range(numvert)] for y in range(numvert)]
    
    cont = 2*numvert
    
    for i in range(0,numvert):
        a[i][(i+1)%numvert] = 1
        a[i][(i-1)%numvert] = 1
        
    a[0][numvert-1] = 1
    a[numvert-1][0] = 1
    for i in range(0,numvert+1):
        for j in range(0,numvert+1):
            if i == numvert or j == numvert:
                a[i][j] = 1
                
    a[numvert][numvert] = 0
    
    for j in range (numvert):
        print(a[j])
        
    mats[numamts][0] = "Roda_" + str(numvert)
    mats[numamts][1] = a
        
    print("O valor de |E|: " + str(cont))
    with open("Roda_" + str(numvert) + '.txt', 'w+') as testfile:
            for row in a:
                testfile.write(' '.join([str(a) for a in row]) + '\n')

def criaCubo():
    
    a = []
    n = input("Insira o valor de n:")
    if(n.isnumeric() == False):
        print("Insira um numero valido.")
        exit()

    
    if int(n) == 0:
        a[0][0] = 0
        cont = 0

        for i in range(0,2**int(n)):
            for j in range(0,2**int(n)):
                print(a[i][j], end= ' ')
            print()
            
        print("O valor de |E|: " + str(n))
        
        mats[numamts][0] = "Cubo_" + str(n)
        mats[numamts][1] = a
        
        with open("Cubo_" + str(n) + '.txt', 'w+') as testfile:
            for row in a:
                testfile.write(' '.join([str(a) for a in row]) + '\n')
        
    elif int(n) == 1:
        a[0][0] = 0
        a[0][1] = 1
        a[1][0] = 1
        a[1][1] = 0
        cont = 1

        for i in range(0,2**int(n)):
            for j in range(0,2**int(n)):
                print(a[i][j], end= ' ')
            print()
            
        mats[numamts][0] = "Cubo_" + str(n)
        mats[numamts][1] = a
            
        print("O valor de |E|: " + str(cont))
        with open("Cubo_" + str(n) + '.txt', 'w+') as testfile:
            for row in a:
                testfile.write(' '.join([str(a) for a in row]) + '\n')

    else:
        for i in range(0,2**int(n)):
            for j in range(0,2**int(n)):
                if a[j][i] == 0:
                    next
                else:
                    a[i][j] = 0
                    a[j][i] = 0
                    
        cont = (2**(int(n)))*int(n)
        
        for i in range(0,2**int(n)):
            for j in range(0,int(n)):
                if ((i >> j) & 1) == 0:
                    v = i + (1 << j)
                    if v < 2**int(n):
                        a[i][v] = 1
                        a[v][i] = 1 
                else:
                    v = i - (1 << j)
                    if v >= 0:
                        a[i][v] = 1
                        a[v][i] = 1
                        
        cont = cont//2

        for i in range(0,2**int(n)):
            for j in range(0,2**int(n)):
                print(a[i][j], end= ' ')
            print()
            
        mats[numamts][0] = "Cubo_" + str(n)
        mats[numamts][1] = a
            
        print("O valor de |E|: " + str(cont))
        with open("Cubo_" + str(n) + '.txt', 'w+') as testfile:
            for row in a:
                testfile.write(' '.join([str(a) for a in row]) + '\n')
                
def buscaLargura():
    
    nome = input("Favor digitar o nome do grafo a ser procurado")
    
    encontrado = False
    
    if mats[0][0] == nome:
        a = mats[0][1]
        
    else:
        
        for i in range (1, len(mats)):
            if mats[i][0] == nome:
                a = mats[i][1]
                encontrado = True
                
                for k in range(0,len(a[i][1])):
                    for j in range(0,len(a[i][1])):
                        
                        print(a[i][1][k][j], end= ' ')

                break
            
    if encontrado == True:
       
        conexo = False
        visitados = []
        fila = Queue()
        fila.put(0) 
        
        while not fila.empty():
            no = fila.get()     
            
            if no not in visitados:
                visitados.append(no)
                vizinhos = []       
                
                for i in range(len(a)):
                    if a[no][i] == 1:
                        vizinhos.append(i) 
                               
                for vizinho in vizinhos:
                    fila.put(vizinho)
                    
        if len(visitados) == len(a):
            conexo = True           
            
        comp_conexas = len(visitados) - 1
        
        if conexo == True:
            print("O grafo eh conexo e tem " + str(comp_conexas) + " componentes conexas")
            
        else:
            print("O grafo nao eh conexo")
    
    else:
        return None
    
    
                
                
print("_____________________________________________________")
print("|                                                   |")
print("|  1 - Grafo normal             2 - Grafo Completo  |")
print("|  3 - Grafo Bipartido          4 - Grafo Estrela   |")
print("|  5 - Grafo Caminho            6 - Grafo Ciclo     |")
print("|  7 - Grafo Roda               8 - Grafo Cubo      |")
print("|  9 - Busca em Largura         0 - Sair            |")
print("|___________________________________________________|")

opc = 10
mats = []

while opc != 0:
    opc = int(input("Escolha o que deseja fazer (opcoes invalidas seram tratadas como 'sair')"))
    numamts = 0
    
    if opc == 1:
        criaGrafoNormal()
        numamts = numamts + 1
        
    elif opc == 2:
        criaCompleto()
        numamts = numamts + 1
    
    elif opc == 3:
        criaBipartido()
        numamts = numamts + 1
    
    elif opc == 4:
        criaEstrela()
        numamts = numamts + 1
        
    elif opc == 5:
        criaCaminho()
        numamts = numamts + 1
        
    elif opc == 6:
        criaCiclo()
        numamts = numamts + 1
        
    elif opc == 7:
        criaRoda()
        numamts = numamts + 1
        
    elif opc == 8:
        criaCubo()
        numamts = numamts + 1
    
    elif opc == 9:
        buscaLargura()
        
    else:
        print("Programa encerrado com sucesso.")
        opc = 0