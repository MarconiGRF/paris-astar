from objetos.estacao import Estacao
from utils.utilities import Utils


def by_f(no):
    return no.f


def limpar_fronteira(fronteira, visitados):
    for no in fronteira:
        removivel_tal_qual_pendrive = -1
        if no in visitados:
            fronteira.remove(no)


def run_astar(origem, destino):
    atual = None

    visitados = []
    fronteira = []

    origem = Estacao(origem)
    destino = Estacao(destino)

    fronteira.append(origem)

    while len(fronteira) != 0 or atual != destino:
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
        elif len(atual.vizinhos) == 1 and len(visitados) != 0 and Estacao(atual.vizinhos[0]) == visitados[len(visitados) - 1]: #situacao em que chegamos a um beco sem saida
            if atual in visitados:
                visitados.remove(atual)
            atual = visitados[len(visitados) - 1]
        else:
            fronteira = []
            for no in atual.vizinhos:
                fronteira.append(Estacao(no))
            if atual:
                if atual not in visitados:
                    visitados.append(atual)
                limpar_fronteira(fronteira, visitados)

    print('O caminho final é o seguinte: ')
    for no in visitados:
        print(str(no) + ' -> ', end='')
    print(str(atual))

    visitados.append(atual)
    print(f'\nO tempo médio vai ser de {Utils.calcular_tempo_total(visitados)}.')


if __name__ == '__main__':
    origem = input("Qual a origem?")
    destino = input("Qual o destino?")

    run_astar(origem, destino)