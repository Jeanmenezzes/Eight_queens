"""
Você deve resolver o clássico exercício das 8 rainhas
Nele o usuário lhe passa o tamanho do tabuleiro n
(lembrar que tabuleiros são quadrados então o usuário
só precisa lhe passar um inteiro) e você deve gerar
uma a uma, todas as distribuições de n rainhas neste tabuleiro
e imprimi-las de uma forma que nenhuma delas ataque a outra,
ou seja, é necessário que duas damas quaisquer não estejam
numa mesma linha, coluna, ou diagonal.

Veja o livro Beginning Python, na descrição
do video para a explicação da solução, ou entre
no dropbox para ver a solução comentada

Esse exercício não é fácil!!
Não se preocupe se você não conseguir
"""
'''
A arquitetura do programa vai se basear em números reais, assim cada casa do tabuleiro irá
gerar uma casa seguinte com um número maior, sendo a primeira casa 1, segunda 2 e assim por
diante.
O tabuleiro irá crescer pelas colunas e depois pelas linhas, sendo a casa 1 primeira linha
e primeira coluna, a casa 2 a primeira linha e segunda coluna, assim por diante.
Em um tabileiro 8x8 por exemplo a casa 9 será a segunda linha e primeira coluna.
O software será um algoritmo de força bruta que irá retornar os tabuleiros com uma função de
impressão própria toda a vez que o programa encontrar um padrão onde o mesmo número rainhas puder
ser inserido na mesma proporção do tabuleiro sem que elas se ameaçem.
'''


#INÍCIO
#ESPECIFICAÇÕES
"""
Variáveis serão feitas no seguinte formato:
variavel_Um_Dois_Tres

Funções serão feitas no seguinte formato:
funcaoUmDoisTres
"""

#RESOLUÇÃO
'''

'''

#PRÓXIMAS ETAPAS DO PROGRAMADOR:
#Corrigir os erros referentes ao loop coluna de insereRainha, onde ele não reinicia o próximo ciclo do 0 e sim do valor referente à posição inicial em coluna.
#Corrigir o erro na geração da lista casas_Maximas que necessita realizar dois loops paralelos e não apenas um loop referente ao tabuleiro_Q
"""

"""

#COMO SERÁ FEITO
"""

"""

#APÓS FINALIZAR AS ETAPAS ANTERIORES:
'''
Criar um algoritmo que altere as verificações de forma a tornar o programa mais eficiente e sem pular nenhuma possibilidade.
Desenvolver uma interface gráfica que mostre toda a sequência de oito rainhas que for encontrada e que conte o número de verificações.
Verificar o algoritmo com a propriedade de conter uma linha por rainha, fazendo com que ao existir uma linha cheia a verificação pare e parta para a próxima.
Verificar se é mais vantajoso fazer o programa com uma lista de casas não ameaçadas, e assim que se adicionar uma nova rainha ir removendo essas casas e as inserindo em uma
lista com as casas ameaçadas.
'''

#EXECUÇÃO DO PROGRAMA
#Importa-se o debugador do programa
import pdb

#Função responsável por inserir as rainhas que não serão alteradas, dentro do tabuleiro_Q e marcar as casas que estão ameaçadas por essas rainhas.
def insereRainha(rainha, tabuleiro_Q):

    linha = (rainha - 1) // 8
    coluna = (rainha % 8) -1

    #Converte a linha da rainha a ser inserida em casas ameaçadas.
    tabuleiro_Q[linha] = [1 for x in range(8)]

    #Converte a coluna da rainha a ser inserida em casas ameaçadas.
    for i in range(len(tabuleiro_Q)):
        tabuleiro_Q[i][coluna] = 1

    #Converte a diagonal superior esquerda da rainha em casas ameaçadas.
    #Cria uma variável auxiliar (mult) para representar a coluna.
    mult = 0
    #Realiza um ciclo subindo as linhas do tabuleiro até a linha de indice 0.
    for linhaMenos in range(linha -1, -1, -1):
        mult += 1
        #Realiza uma verificação onde caso a coluna antecessora não atinja um valor menor que a coluna 0 a casa será ameaçada.
        if coluna - mult >= 0:
            tabuleiro_Q[linhaMenos][coluna - mult] = 1
        else:
            break
    
    #converte a diagonal superior direita da rainha em casas ameaçadas
    #Cria uma variável auxiliar (mult) para representar a coluna.
    mult = 0
    #Realiza um ciclo subindo as linhas do tabuleiro até a linha de indice 0.
    for linhaMenos in range(linha -1, -1, -1):
        mult += 1
        #Realiza uma verificação onde caso a coluna sucessora não atinja um valor maior que a coluna 7 a casa será ameaçada.
        if coluna + mult <= 7:
            tabuleiro_Q[linhaMenos][coluna + mult] = 1
        else:
            break
        
    #converte a diagonal inferior esquerda da rainha em casas ameaçadas
    #Cria uma variável auxiliar (mult) para representar a coluna.
    mult = 0
    #Realiza um ciclo descendo as linhas do tabuleiro até a linha de indice 7.
    for linhaMais in range(linha +1, 8):
        mult += 1
        #Realiza uma verificação onde caso a coluna antecessora não atinja um valor menor que a coluna 0 a casa será ameaçada.
        if coluna - mult >= 0:
            tabuleiro_Q[linhaMais][coluna - mult] = 1
        else:
            break
    
    #converte a diagonal inferior direita da rainha em casas ameaçadas
    #Cria uma variável auxiliar (mult) para representar a coluna.
    mult = 0
    #Realiza o ciclo descendo as linhas do tabuleiro até a linha de indice 7.
    for linhaMais in range(linha +1, 8):
        mult += 1
        #Realiza uma verificação onde caso a coluna sucessora não atinja um valor maior que a coluna 7 a casa será ameaçada.
        if coluna + mult <= 7: 
            tabuleiro_Q[linhaMais][coluna + mult] = 1
        else:
            break

    #Marca a posição final de todas as rainhas ameaçadas
    tabuleiro_Q[linha][coluna] = 'Q'
    return tabuleiro_Q

#Retorna a sequência que dará início em insereRainha, a sequência casas_Maximas atualizada com o respectivo número de rainhas da sequência que
#será usada em insereRainha, e o valor da última casa que foi descartada e não poderá ter nenhum valor menor ou igual a ela na próxima rainha inserida (contador).
def proximaSequencia(ultimo_Tabuleiro, tamanho_UTN, casas_Maximas):
    #Bloco Try é criado pois é possível que o último tabuleiro esteja vazio (se ele for o primeiro), o que geraria um erro do tipo Index.
    try:
        #Tabalha com a possibilidade da última rainha ter alcançado o valor máximo para a sua posição (a partir de cassas_Maximas) e então ter que alterar a
        #posição da penúltima rainha inserida.
        if ultimo_Tabuleiro[tamanho_UTN - 1] == casas_Maximas[tamanho_UTN - 1]:
            #Retorna proxima_Sequencia_Inicio, casas_Maximas e contador
            return ultimo_Tabuleiro[:-2] , casas_Maximas[:-1], ultimo_Tabuleiro[-2]
        #Trabalha com a exclusão apenas da última rainha, o que dá continuidade no loop apenas alterando ela.
        else:
            #Também retorna proxima_Sequencia_Inicio, casas_Maximas e contador
            return ultimo_Tabuleiro[:-1], casas_Maximas, ultimo_Tabuleiro[-1] 
    except IndexError:
        #O tabuleiro_N só será negativo no caso da primeira verificação, então são retornados as variáveis para o programa realizar o primeiro ciclo.
        #Em todas as demais verificações mesmo que a primeira rainha seja excluída por proximaSequencia, nunca insereRainha retornará uma sequência vazia.
        return [], casas_Maximas, 0

#Função responsável por retornar o tabuleiro_N com uma nova distribuição de rainhas e atualizar casas_Maximas com as casas máximas das novas rainhas inseridas.
def criaTabuleiro(proxima_Sequencia_Inicio, tabuleiro_Q, contador, casas_Maximas):
    #Cria uma lista auxiliar igual ao proxima_Sequencia_Inicio, onde serão adicionadas as novas rainhas.
    tabuleiro_Adicionar_N = proxima_Sequencia_Inicio

    #Define a variável coluna a partir de (contador), a qual conterá o índice da coluna da última rainha adicionada.
    coluna = contador%8

    #Define a variável linha a partir de um condicional onde caso o índice de início da verificação de onde será inserida a próxima rainha (contador) efetuado
    #o cálculo de divisão inteira para representar a linha que será iniciado, destacar que é o mesmo valor de indice de linha onde está a última rainha inserida
    #então o valor do indice de linha será ampliado para a linha seguinte de tabuleiro_Q, pois todas as casas da linha da rainha já estarão ameaçadas.
    if (contador -1) // 8 == contador // 8:
        linha = (contador // 8) + 1
        contador += 8 - coluna 
    else:
        linha = contador // 8 
    
    #Algoritmo para verificar se uma posição não está ameaçada pelas rainhas, caso não esteja ele insere uma nova rainha e marca todas as casas que ameaçar
    for i in range(linha, 8):
        for j in range(8):
            if tabuleiro_Q[i][j] == 0:
                #marca as casas ameaçadas na mesma linha da rainha
                tabuleiro_Q[i] = [1 for g in range(8)]
                tabuleiro_Q[i][j] = "Q"
                tabuleiro_Adicionar_N.append(contador + 1)
                #marca as casas ameaçadas na mesma coluna da rainha
                for k in range(8):
                    if tabuleiro_Q[k][j] != "Q":
                        tabuleiro_Q[k][j] = 1

                #Este trecho marca as casas ameaçadas na mesma diagonal da rainha
                #Redefine as variáveis linha e coluna para marcar a posição atual da rainha que foi inserida.
                linha = contador // 8
                coluna = (contador%8) - 1

                #Cria uma variável auxiliar mult que irá variar a medida que não estiver no loop (vertical ou horizontal).
                mult = 0

                #Faz a modificação das diagonais em quatro loops diferentes, sempre partindo da casa da rainha e avançando da diagonal pra cima e pra trás,
                #pra cima e pra frente, pra tras e pra baixo, pra baixo e pra frente.
                for linhaMenos in range(linha-1, -1, -1):
                    mult += 1
                    try:
                        if coluna - mult >= 0:
                            tabuleiro_Q[linhaMenos][coluna - mult] = 1
                    except IndexError:
                        break
                mult = 0
                for linhaMenos in range(linha-1, -1, -1):
                    mult += 1
                    try:
                        tabuleiro_Q[linhaMenos][coluna + mult] = 1
                    except IndexError:
                        break
        
                mult = 0
                for linhaMais in range(linha+1,8):
                    mult += 1
                    try:
                        if coluna - mult >= 0:
                            tabuleiro_Q[linhaMais][coluna - mult] = 1
                    except IndexError:
                        break

                mult = 0
                for linhaMais in range(linha+1,8):
                    mult += 1
                    try:
                        tabuleiro_Q[linhaMais][coluna + mult] = 1
                    except IndexError:
                        break

                #Após o tabuleiro_Q ter sido completamente implementado pela inserção da rainha de valor igual à variável contador, é criada uma outra
                #variável casa_Maxima que representa o valor máximo que a próxima rainha poderá assumir
                casa_Maxima = False
                contador_Casa_Maxima = contador
                for linha_em_Q in range(linha, 8):
                    for coluna_em_Q in range(8):
                        if tabuleiro_Q[linha_em_Q][coluna_em_Q] == 0:
                            casa_Maxima = contador_Casa_Maxima + 1
                if not casa_Maxima:
                    pass
                else:
                    casas_Maximas.append(casa_Maxima)
                
                #Soma ao contador todos os números de casas seguintes da linha onde a rainha foi inserida e na sequência
                #encerra o ciclo referente à linha, evitando assim o desperdício de processamento com algumas verificações

                #TALVEZ EXISTA UM ERRO AQUI REFERENTE À CASA E À POSIÇÃO DA CASA DE CONTADOR.
                contador += 9 - coluna
                break

                """ USADO PARA IMPRIMIR OS TABULEIROS COMPLETOS
                for z in range(8):
                    print(tabuleiro_Q[z])
                print("\n")
                """
            contador += 1
    tabuleiro_N.append(tabuleiro_Adicionar_N)
    return tabuleiro_N, casas_Maximas

def funcaoGeradora(tabuleiro_N, tabuleiro_Q, casas_Maximas):

    #Define a posição da última sequência contida em tabuleiro_N, o valor nunca será menor que 0 pois tabuleiro_N é criado já com uma sequência vazia.
    pos_Ultima_Sequencia_N = len(tabuleiro_N) -1

    #Define o último tabuleiro de N, que será o ponto de partida para verificar qual a próxima sequência que terá uma rainha inserida.
    ultimo_Tabuleiro_N = tabuleiro_N[pos_Ultima_Sequencia_N]

    #Marca o tamanho do último tabuleiro de N, que facilitará o uso e entendimento dessa variável dentro da função proximaSequencia.
    tamanho_UTN = len(ultimo_Tabuleiro_N)

    #Gera o início de onde será implementada a próxima sequência de tabuleiro_N (proxima_Sequencia_Inicio), atualiza a lista contendo as casas limite para
    #cada nova rainha ser inserida dentro de insereRainha (casas_Maximas), e dá o ponto de partida para insereRainha iniciar as verificações (contador).
    proxima_Sequencia_Inicio, casas_Maximas, contador = proximaSequencia(ultimo_Tabuleiro_N, tamanho_UTN, casas_Maximas)

    #Utiliza da sequência proxima_Sequencia_Inicio para preencher tabuleiro_Q de forma que ele marque todas as casas que estão ameaçadas por essas rainhas.
    for rainha in proxima_Sequencia_Inicio:
        tabuleiro_Q = insereRainha(rainha, tabuleiro_Q)
    
    tabuleiro_N, casas_Maximas = criaTabuleiro(proxima_Sequencia_Inicio, tabuleiro_Q, contador, casas_Maximas)

    yield tabuleiro_N, casas_Maximas

#Função principal de execução do programa.
def main():
    #Cria as variáveis:

    #tabuleiro_Q que conterá o diagrama das rainhas e das casas ameaçadas (de 1 a 64).
    tabuleiro_Q = [[0 for x in range(8)] for x in range(8)]
    
    #tabuleiro_N que conterá todas as distribuições de rainhas que já foram encontradas, considerando como 1 para a posição 0 de tabuleiro_Q.
    tabuleiro_N = [[]]
    
    #casas_Maximas é uma lista contendo todo o valor máximo que cada rainha sucessora (1ª,2ª, 3ª, ..., 8ª) poderá conter de acordo com a distribuição
    #anterior, como a primeira rainha é livre de distribuições anteriores ela assume o valor máximo 64, as demais poderão variar de acordo com a distribuição vigente.
    casas_Maximas = [64]

    #Loop que inicia a função geradora, ele irá percorrer pelo número de casas possíveis para as rainhas serem alocadas
    #Número 20 assumido para teste do programa.
    for i in range(20):
        #Executa a função geradora onde cada loop retorna a lista de tabuleiro_N implementada com um novo ordenamento de distribuição de rainhas e casasMaximas
        #que é substituída pela nova lista referente à sua função para o novo (último) valor de tabuleiro_N.
        tabuleiro_N, casas_Maximas = funcaoGeradora(tabuleiro_N, tabuleiro_Q, casas_Maximas)

        #No momento só printa no IDLE o valor da nova distribuição de tabuleiro_N, mas esse valor será usado para implementar as próximas funções do programa.
        print(tabuleiro_N[len(tabuleiro_N) - 1])

if __name__ == '__main__':
    main()
    

#PROBLEMA GERAL
#CORRIGIR O CÓDIGO DE insereRainha DE ACORDO COM OS NOVOS PARADIGMAS DO PROGRAMA GERAL.
#IMPLEMENTAR O CÓDIGO DE main DE FORMA QUE SEJA POSSÍVEL USAR AS PROPRIEDADES DE FUNÇÃO GERADORA DE insereRainha.
#CASO NÃO SEJA POSSÍVEL APROVEITAR DAS PROPRIEDADES DE FUNÇÃO GERADORA DE insereRainha REESCREVER O CÓDIGO DENTRO DA PRÓPRIA FUNÇÃO insereRainha
#DEFINIR O QUE VAI ACONTECER CASO TODAS AS VERIFICAÇÕES SEJAM FEITAS E proximaSequencia DEVOLVA UMA LISTA VAZIA IGUAL À PRIMEIRA LISTA.




