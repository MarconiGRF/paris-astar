class Distancias:

    def __init__(self):
        self.diretas = [
            [ 0, 10, 18.5, 24.8, 36.4, 38.8, 35.8, 25.4, 17.6,  9.1, 16.7, 27.3, 27.6, 29.8],
            [-1,  0,  8.5, 14.8, 26.6, 29.1, 26.1, 17.3,   10,  3.5, 15.5, 20.9, 19.1, 21.8],
            [-1, -1,    0,  6.3, 18.2, 20.6, 17.6, 13.6,  9.4, 10.3, 19.5, 19.1, 12.1, 16.6],
            [-1, -1,   -1,    0,   12, 14.4, 11.5, 12.4, 12.6, 16.7, 23.6, 18.6, 10.6, 15.4],
            [-1, -1,   -1,   -1,    0,    3,  2.4, 19.6, 23.3, 28.2, 34.2, 24.8, 14.5, 17.9],
            [-1, -1,   -1,   -1,   -1,    0,  3.3, 22.3, 25.7, 30.3, 36.7, 27.6, 15.2, 18.2],
            [-1, -1,   -1,   -1,   -1,   -1,    0,   20,   23, 27.3, 34.2, 25.7, 12.4, 15.6],
            [-1, -1,   -1,   -1,   -1,   -1,   -1,    0,  8.2, 20.3, 16.1,  6.4, 22.7, 27.6],
            [-1, -1,   -1,   -1,   -1,   -1,   -1,   -1,    0, 13.5, 11.2, 10.9, 21.2, 26.6],
            [-1, -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,    0, 17.6, 24.2, 18.7, 21.2],
            [-1, -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,    0, 14.2, 31.5, 35.5],
            [-1, -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,    0, 28.8, 33.6],
            [-1, -1,   -1,   -1,   -1,   -1,    0,   -1,   -1,   -1,   -1,   -1,    0,  5.1],
            [-1, -1,   -1,   -1,   -1,   -1,    0,   -1,   -1,   -1,   -1,   -1,   -1,    0],
        ]
        self.reais = [
            [0,  10,  -1,  -1,  -1,  -1,  -1,   -1,  -1,  -1,   -1,  -1,   -1,  -1],
            [-1,  0, 8.5,  -1,  -1,  -1,  -1,   -1,  10, 3.5,   -1,  -1,   -1,  -1],
            [-1, -1,   0, 6.3,  -1,  -1,  -1,   -1, 9.4,  -1,   -1,  -1, 18.7,  -1],
            [-1, -1,  -1,   0,  13,  -1,  -1, 15.3,  -1,  -1,   -1,  -1, 12.8,  -1],
            [-1, -1,  -1,  -1,   0,   3, 2.4,   30,  -1,  -1,   -1,  -1,   -1,  -1],
            [-1, -1,  -1,  -1,  -1,   0,  -1,   -1,  -1,  -1,   -1,  -1,   -1,  -1],
            [-1, -1,  -1,  -1,  -1,  -1,   0,   -1,  -1,  -1,   -1,  -1,   -1,  -1],
            [-1, -1,  -1,  -1,  -1,  -1,  -1,    0, 9.6,  -1,   -1, 6.4,   -1,  -1],
            [-1, -1,  -1,  -1,  -1,  -1,  -1,   -1,   0,  -1, 12.2,  -1,   -1,  -1],
            [-1, -1,  -1,  -1,  -1,  -1,  -1,   -1,  -1,   0,   -1,  -1,   -1,  -1],
            [-1, -1,  -1,  -1,  -1,  -1,  -1,   -1,  -1,  -1,    0,  -1,   -1,  -1],
            [-1, -1,  -1,  -1,  -1,  -1,  -1,   -1,  -1,  -1,   -1,   0,   -1,  -1],
            [-1, -1,  -1,  -1,  -1,  -1,  -1,   -1,  -1,  -1,   -1,  -1,    0, 5.1],
            [-1, -1,  -1,  -1,  -1,  -1,  -1,   -1,  -1,  -1,   -1,  -1,   -1,   0],
        ]
        self.vizinhos = {
            "E1": ["E2"],
            "E2": ["E1", "E3", "E9", "E10"],
            "E3": ["E2", "E4", "E9", "E14"],
            "E4": ["E3", "E5", "E8", "E13"],
            "E5": ["E4", "E6", "E7", "E8"],
            "E6": ["E5"],
            "E7": ["E5"],
            "E8": ["E4", "E5", "E9", "E12"],
            "E9": ["E2", "E3", "E8", "E11"],
            "E10": ["E2"],
            "E11": ["E9"],
            "E12": ["E8"],
            "E13": ["E3", "E4", "E14"],
            "E14": ["E13"],
        }
        self.linhas = {
            "E1": ["azul"],
            "E2": ["azul", "amarela"],
            "E3": ["azul", "vermelha"],
            "E4": ["azul", "verde"],
            "E5": ["azul", "amarela"],
            "E6": ["azul"],
            "E7": ["amarela"],
            "E8": ["amarela", "verde"],
            "E9": ["amarela", "vermelha"],
            "E10": ["amarela"],
            "E11": ["vermelha"],
            "E12": ["verde"],
            "E13": ["vermelha", "verde"],
            "E14": ["verde"],
        }
