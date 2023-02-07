from estaticos.distancias import Distancias

class Estacao:
    """
    Representa cada estação através de características essenciais tais quais:
    - formal: Nome formal do nó (ex: E1, E2, E3)
    - vizinhos: Seus vizinhos
    - linha: Linha a qual pertence (ex: azul, amarela, etc)
    """

    def __init__(self, nome_formal=None):
        self.formal = nome_formal

        self.vizinhos = Distancias().vizinhos[nome_formal]
        self.linha = Distancias().linhas[nome_formal]

        self.f = 0
        self.g = 0
        self.h = 0

    def calcular_g(self, origem, historico_distancia):
        distancia_real = self.get_distancia_real(origem)
        if distancia_real == -1:
            return False
        else:
            self.g = historico_distancia + distancia_real
            return self.g

    def get_distancia_real(self, origem):
        real_linha = int(origem.formal[1:]) - 1
        real_coluna = int(self.formal[1:]) - 1

        distancia_real_normal     = Distancias().reais[real_linha][real_coluna]
        distancia_real_transposta = Distancias().reais[real_coluna][real_linha]

        if distancia_real_normal != -1:
            return distancia_real_normal
        elif distancia_real_transposta != -1:
            return  distancia_real_transposta
        else:
            return False

    def calcular_h(self, destino):
        direta_linha = int(self.formal[1:]) - 1
        direta_coluna = int(destino.formal[1:]) - 1

        distancia_direta_normal     = Distancias().diretas[direta_linha][direta_coluna]
        distancia_direta_transposta = Distancias().diretas[direta_coluna][direta_linha]

        if distancia_direta_normal != -1:
            self.h = distancia_direta_normal
        else:
            self.h = distancia_direta_transposta

        return self.h

    def __eq__(self, other):
        return self.formal == other.formal

    def __str__(self):
        return self.formal
