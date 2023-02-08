
class Utils:

    @staticmethod
    def time_format(seconds: int) -> str:
        if seconds is not None:
            seconds = int(seconds)
            d = seconds // (3600 * 24)
            h = seconds // 3600 % 24
            m = seconds % 3600 // 60
            s = seconds % 3600 % 60
            if d > 0:
                return '{:02d}D {:02d}H {:02d}m {:02d}s'.format(d, h, m, s)
            elif h > 0:
                return '{:02d}H, {:02d}m e {:02d}s'.format(h, m, s)
            elif m > 0:
                return '{:02d}m {:02d}s'.format(m, s)
            elif s > 0:
                return '{:02d}s'.format(s)
        return '-'

    @classmethod
    def calcular_baldeacao(cls, visitados):
        tempo_baldeacao_segundos = 240
        tempo_total_baldeacao = 0

        # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        ultima_linha = visitados[0].linha[0]
        for no in visitados:
            if ultima_linha not in no.linha:
                ultima_linha = no.linha[0]
                tempo_total_baldeacao += tempo_baldeacao_segundos
        return tempo_total_baldeacao

    @classmethod
    def calcular_tempo_total(cls, visitados):
        distancia_total_km = visitados[len(visitados) - 1].g
        tempo_segundos = (distancia_total_km * 1000) / (30 / 3.6)

        tempo_baldeacao = cls.calcular_baldeacao(visitados)
        return cls.time_format(tempo_segundos + tempo_baldeacao)

    @classmethod
    def print_tempo(cls, visitados, atual):
        visitados.append(atual)
        print(f'\nO tempo médio vai ser de {Utils.calcular_tempo_total(visitados)}.')

    @classmethod
    def print_fronteira(cls, fronteira):
        print(f'\nA fronteira atual é [', end='')
        for no in fronteira[:-1]:
            print(str(no) + ', ', end='')
        print(f'{fronteira[len(fronteira) - 1]}]')

    @classmethod
    def print_final(cls, visitados, atual):
        print('\nO caminho final é o seguinte: ')
        acumulador = []

        for (index, no) in enumerate(visitados[:-1]):
            if visitados[index + 1].formal in no.vizinhos:
                acumulador.append(visitados[index])
        acumulador.append(visitados[len(visitados) - 1])
        acumulador.append(atual)

        for no in acumulador[:-1]:
            print(str(no) + ' -> ', end='')
        print(str(acumulador[len(acumulador) - 1]))

        cls.print_tempo(acumulador, atual)
