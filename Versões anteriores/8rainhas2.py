tabuleiro_1 = [[0 for x in range(8)] for x in range(8)]
tabuleiro_2 = []
for x in range(8):
    print(tabuleiro_1[x])
def insereRainha(tabuleiro_Q, tabuleiro_N):
    #Algoritmo para verificar se uma posição não está ameaçada pelas rainhas, caso não esteja ele insere
    #uma nova rainha e marca todas as casas que ameaçar
    contador = 0
    for i in range(8):
        for j in range(8):
            contador += 1
            if tabuleiro_Q[i][j] == 0:
                tabuleiro_Q[i] = [1 for g in range(8)]
                tabuleiro_Q[i][j] = "Q"
                tabuleiro_N.append(contador)
                for k in range(8):
                    if tabuleiro_Q[k][j] != "Q":
                        tabuleiro_Q[k][j] = 1
    print(tabuleiro_N)
    for x in range(8):
        print(tabuleiro_Q[x])
