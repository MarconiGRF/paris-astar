from objetos.estacao import Estacao


def by_f(no):
    return no.f


def limpar_fronteira(fronteira, visitados):
    for no in fronteira:
        removivel_tal_qual_pendrive = -1
        try:
            removivel_tal_qual_pendrive = visitados.index(no)
        except ValueError:
            removivel_tal_qual_pendrive = -1

        if removivel_tal_qual_pendrive != -1:
            fronteira.pop(removivel_tal_qual_pendrive)


def run_astar(origem, destino):
    atual = None

    #lista de estacoes ja visitadas e de estacoes de fronteira
    visitados = []
    fronteira = []

    #fronteira.append(Estacao(origem))

    origem = Estacao(origem)
    destino = Estacao(destino)

    fronteira.append(origem)

    while len(fronteira) != 0 or atual != destino:
        if atual:
            if atual not in visitados:
                visitados.append(atual)
            limpar_fronteira(fronteira, visitados)

        for no in fronteira:
            if atual:
                valor_g = no.calcular_g(atual, atual.g)
            else:
                valor_g = no.calcular_g(origem, 0)
            valor_h = no.calcular_h(destino)
            no.f = valor_g + valor_h


        fronteira.sort(key=by_f)
        atual = fronteira.pop(0)

        if atual == destino:
            break
        elif atual != destino and len(atual.vizinhos) == 1 and len(visitados) != 0 and Estacao(atual.vizinhos[0]) == visitados[len(visitados) - 1]: #situacao em que chegamos a um beco sem saida
            if atual in visitados:
                visitados.remove(atual) #removes the useless station
            atual = visitados[len(visitados) - 1] #links de current value to the previous node in stack
        else:
            fronteira = []
            for no in atual.vizinhos:
                fronteira.append(Estacao(no))

    for no in visitados:
        print(str(no) + ' -> ', end='')
    print(str(atual))
if __name__ == '__main__':
    origem = input("Qual a origem?")
    destino = input("Qual o destino?")

    run_astar(origem, destino)