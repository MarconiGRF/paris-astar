from objetos.estacao import Estacao


def by_f(no):
    return no.f


def limpar_fronteira(fronteira, visitados):
    for no in fronteira:
        removivel_tal_qual_pendrive = -1
        try:
            removivel_tal_qual_pendrive = visitados.index(no.formal)
        except ValueError:
            removivel_tal_qual_pendrive = -1

        if removivel_tal_qual_pendrive != -1:
            fronteira.pop(removivel_tal_qual_pendrive)


def run_astar(origem, destino):
    atual = None
    visitados = []

    fronteira = []
    fronteira.append(Estacao(origem))

    origem = Estacao(origem)
    destino = Estacao(destino)

    while len(fronteira) != 0 or atual != destino:
        if atual:
            visitados.append(atual.formal)

        for no in fronteira:
            if atual:
                valor_g = no.calcular_g(origem, atual.g)
            else:
                valor_g = no.calcular_g(origem, 0)
            valor_h = no.calcular_h(destino)
            no.f = valor_g + valor_h

        limpar_fronteira(fronteira, visitados)

        fronteira.sort(key=by_f)
        atual = fronteira.pop(0)

        if atual == destino:
            break
        else:
            for no in atual.vizinhos:
                fronteira.append(Estacao(no))

if __name__ == '__main__':
    origem = input("Qual a origen?")
    destino = input("Qual o destino?")

    run_astar(origem, destino)
