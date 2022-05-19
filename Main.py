import Grafo
#0 - preto
#1 - branco
#2 - verde
#3 - vermelho

'''
A lista cores indica o numero referente a cor de cada vertice
inicialmente todos os vertices sao setados como preto

'''

cores = [0]*15


def validacao(grafo, cor, cont):
    for adj in grafo.grafo[cont]:
        if(cores[adj-1] == cor):
            return False
    return True


def coloracao(grafo, tamanho, cont):
    if(cont == tamanho-1):
        return True
    for cor in range(4):

        if (validacao(grafo, cor, cont)):

            cores[cont] = cor
            if(coloracao(grafo, tamanho, cont=cont+1)):
                return True

    return False


g = Grafo.grafo(15)
# Adiciona as arestas contidas no arquivo txt
g.leitura_arquivo(g, 'grafo_teste.txt')

if(coloracao(g, 15, 0)):
    print('É possivel fazer a coloração')
    i = 1
    for cor in cores:
        if(cor == 0):
            print("Vertice:"+str(i)+" - Preto")
            i += 1
        elif(cor == 1):
            print("Vertice:"+str(i)+"- Branco")
            i += 1
        elif(cor == 2):
            print("Vertice:"+str(i)+"- Verde")
            i += 1
        else:
            print("Vertice:"+str(i)+"- Vermelho")
            i += 1

else:
    print('Nao é possível fazer a coloração do grafo')
    for c in range(len(cores)):
        cores[c] = 0
