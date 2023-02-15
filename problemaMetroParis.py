# - E1 E2 E3 E4 E5 E6 E7 E8 E9 E10 E11 E12 E13 E14
# E1 - 11 20 27 40 43 39 28 18 10 18 30 30 32
# E2 11 - 9 16 29 32 28 19 11 4 17 23 21 24
# E3 20 9 - 7 20 22 19 15 10 11 21 21 13 18
# E4 27 16 7 - 13 16 12 13 13 18 26 21 11 17
# E5 40 29 20 13 - 3 2 21 25 31 38 27 16 20
# E6 43 32 22 16 3 - 4 23 28 33 41 30 17 20
# E7 39 28 19 12 2 4 - 22 25 29 38 28 13 17
# E8 28 19 15 13 21 23 22 - 9 22 18 7 25 30
# E9 18 11 10 13 25 28 25 9 - 13 12 12 23 28
# E10 10 4 11 18 31 33 29 22 13 - 20 27 20 23
# E11 18 17 21 26 38 41 38 18 12 20 - 15 35 39
# E12 30 23 21 21 27 30 28 7 12 27 15 - 31 37
# E13 30 21 13 11 16 17 13 25 23 20 35 31 - 5
# E14 32 24 18 17 20 20 17 30 28 23 39 37 5 -


distMetro = [
    [0, 11, 20, 27, 40, 43, 39, 28, 18, 10, 18, 30, 30, 32],
    [11, 0, 9, 16, 29, 32, 28, 19, 11, 4, 17, 23, 21, 24],
    [20, 9, 0, 7, 20, 22, 19, 15, 10, 11, 21, 21, 13, 18],
    [27, 16, 7, 0, 13, 16, 12, 13, 13, 18, 26, 21, 11, 17],
    [40, 29, 20, 13, 0, 3, 2, 21, 25, 31, 38, 27, 16, 20],
    [43, 32, 22, 16, 3, 0, 4, 23, 28, 33, 41, 30, 17, 20],
    [39, 28, 19, 12, 2, 4, 0, 22, 25, 29, 38, 28, 13, 17],
    [28, 19, 15, 13, 21, 23, 22, 0, 9, 22, 18, 7, 25, 30],
    [18, 11, 10, 13, 25, 28, 25, 9, 0, 13, 12, 12, 23, 28],
    [10, 4, 11, 18, 31, 33, 29, 22, 13, 0, 20, 27, 20, 23],
    [18, 17, 21, 26, 38, 41, 38, 18, 12, 20, 0, 15, 35, 39],
    [30, 23, 21, 21, 27, 30, 28, 7, 12, 27, 15, 0, 31, 37],
    [30, 21, 13, 11, 16, 17, 13, 25, 23, 20, 35, 31, 0, 5],
    [32, 24, 18, 17, 20, 20, 17, 30, 28, 23, 39, 37, 5, 0]
]


#  1 - E1
#  2 - E2
#  3 - E3
#  4 - E4
# ...

# Cidade / Acomulado
estadoInicial = ['e12', 0]
estadoFinal = ['e14', 0]

caminho = []
visitado = []
borda = []

grafo = [
    ['e1', 'e2'],
    ['e2', 'e1'],
    ['e2', 'e10'],
    ['e2', 'e9'],
    ['e2', 'e3'],
    ['e10', 'e2'],
    ['e9', 'e2'],
    ['e9', 'e11'],
    ['e9', 'e8'],
    ['e9', 'e3'],
    ['e11', 'e9'],
    ['e8', 'e12'],
    ['e8', 'e9'],
    ['e8', 'e4'],
    ['e8', 'e5'],
    ['e12', 'e8'],
    ['e3', 'e9'],
    ['e3', 'e2'],
    ['e3', 'e4'],
    ['e3', 'e13'],
    ['e4', 'e3'],
    ['e4', 'e8'],
    ['e4', 'e5'],
    ['e4', 'e13'],
    ['e13', 'e3'],
    ['e13', 'e4'],
    ['e13', 'e14'],
    ['e14', 'e13'],
    ['e5', 'e4'],
    ['e5', 'e6'],
    ['e5', 'e7'],
    ['e7', 'e5'],
    ['e6', 'e5'],
]

def getPosicao(no):
    # print(int(no[1]))
    return int(no[0][1]) - 1

def foiVisitado(no):
    for i in visitado:
        if(no == i[0]):
            return True

    return False

# retorna os vizinhos do nó
def sucessor(no):
    sucessores = []

    for noGrafo in grafo:
        if((no[0] == noGrafo[0]) and (not foiVisitado(noGrafo[1]))):
            sucessores.append([noGrafo[1], 0])

    for suc in sucessores:
        custo = distMetro[getPosicao(no)][getPosicao(suc)]
        heuristica =  distMetro[getPosicao(estadoFinal)][getPosicao(suc)]
        suc[1] += custo + heuristica + no[1]

    
    
    if(len(sucessores) == 0):
        return -1
    else:
        return sucessores

# print(sucessor(estadoInicial))

def paraOndeIr(borda):
    menorCusto = ['', 999]
    
    for no in borda:
        if(no[1] < menorCusto[1]):
            menorCusto = no

    return menorCusto

def buscarMelhorCaminho(grafo):

    # caminho.append(estadoInicial)
    borda.append(estadoInicial)
    # visitado.append(estadoInicial)
    # caminho.append(estadoInicial)
    noDeIda = []
    
    # suces = sucessor(noDeIda)

    # borda.remove(noDeIda)

    # for colocandoNoBorda in suces:
    #     borda.append(colocandoNoBorda)

    while(len(borda) != 0):


        noDeIda = paraOndeIr(borda)
        
        suces = sucessor(noDeIda)

        # borda.remove(noDeIda)
        if(suces == -1):
            borda.remove(noDeIda)
        else:    
            borda.clear()
        # suces = sucessor(borda[len(borda) - 1])

        if(suces != -1):
            for colocandoNoBorda in suces:
                borda.append(colocandoNoBorda)

        visitado.append(noDeIda)
        caminho.append(noDeIda)

        if(noDeIda[0] == estadoFinal[0]):
            break

        if(suces == -1):
            caminho.remove(noDeIda)


    print(caminho)  

        

        
            




buscarMelhorCaminho(grafo)

        

    
