from objetos.estacao import Estacao
from utils.utilities import Utils


def by_f(no):
    return no.f


def limpar_fronteira(fronteira, visitados):
    for no in fronteira:
        if no in visitados:
            fronteira.remove(no)


def backtrack(visitados, atual):
    if atual in visitados:
        visitados.remove(atual)
    return visitados[len(visitados) - 1]


def calcular_valores_heuristicos(fronteira, atual, origem, destino):
    for no in fronteira:
        if atual:
            valor_g = no.calcular_g(atual, atual.g)
        else:
            valor_g = no.calcular_g(origem, 0)
        valor_h = no.calcular_h(destino)
        no.f = valor_g + valor_h


def caminho_via_astar(origem, destino):
    atual = None

    visitados = []
    fronteira = []

    origem = Estacao(origem)
    destino = Estacao(destino)

    fronteira.append(origem)

    while len(fronteira) != 0 or atual != destino:
        calcular_valores_heuristicos(fronteira, atual, origem, destino)

        fronteira.sort(key=by_f)
        Utils.print_fronteira(fronteira)

        atual = fronteira.pop(0)

        caminho_sem_saida = len(atual.vizinhos) == 1 and \
                            len(visitados) != 0 and \
                            Estacao(atual.vizinhos[0]) == visitados[len(visitados) - 1]
        if atual == destino:
            break
        elif caminho_sem_saida:
            atual = backtrack(visitados, atual)
        else:
            fronteira = []
            for no in atual.vizinhos:
                fronteira.append(Estacao(no))
            if atual:
                if atual not in visitados:
                    visitados.append(atual)
                limpar_fronteira(fronteira, visitados)

    Utils.print_final(visitados, atual)


if __name__ == '__main__':
    o = input("Qual a origem?")
    d = input("Qual o destino?")

    caminho_via_astar(o, d)
