class grafo:
    def __init__(self, tamanho):
        self.qtdVertices = tamanho
        self.grafo = [[] for i in range(self.qtdVertices)]

    def adicionar_aresta(self, a, b):

        if(b not in self.grafo[a-1]):
            self.grafo[a-1].append(b)
        if(a not in self.grafo[b-1]):
            self.grafo[b-1].append(a)

    def mostra_grafo(grafo):
        for i in range(grafo.qtdVertices):
            # end='' elimina a quebra de linha
            print(f'{i+1}->', end='  ')
            for j in grafo.grafo[i]:
                print(f'{j}  ->', end='  ')
            print('')

    def leitura_arquivo(grafo, nome_arq):
        # Cada linha do arquivo vira o elemento de uma lista
        linhas = open(nome_arq).read().splitlines()
        for i, linha in enumerate(linhas):
            linhas[i] = [x for x in linha.split() if x != '\n']
        cont = 0
        for linha in linhas:
            if(cont > 3):
                grafo.adicionar_aresta(int(linha[0]), int(linha[1]))
            cont += 1
