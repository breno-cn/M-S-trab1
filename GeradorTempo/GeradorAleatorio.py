import numpy as np

class GeradorAleatorio:

    # Recebe o caminho para um arquivo texto contendo dados iniciais
    # que serão usados para o método Monte Carlo
    def __init__(self, filepath, intervalos):
        self.dadosIniciais = []
        self.dadosIniciaisIntervalados = []
        self.intervalos = intervalos
        self.pontosMedios = []
        self.menor = 0
        self.maior = 0

        with open(filepath) as dados:
            linhas = dados.read().splitlines()
            self.dadosIniciais = np.array(list(map(int, linhas)))
            self.dadosIniciais.sort()
            self.dadosIniciaisIntervalados = np.array_split(self.dadosIniciais, intervalos)

            self.pontosMedios = [int(intervalo.mean()) for intervalo in self.dadosIniciaisIntervalados]

            self.menor = self.dadosIniciais[0]
            self.maior = self.dadosIniciais[-1]

            # print(self.intervalos)
            # print(self.dadosIniciais)
            # print(self.dadosIniciaisIntervalados)
            # print(self.pontosMedios)

    def gerarTempo(self):
        # Gerar um numero aleatorio
        num = np.random.randint(low=self.menor, high=self.maior, size=1)[0]
        # print(f'numero sorteado: {num}')

        # Verificar qual intervalo esse número pertence
        i = 0
        for intervalo in self.dadosIniciaisIntervalados:
            menor = intervalo[0]
            maior = intervalo[-1]

            # intervalo encontrado
            if num >= menor and num <= maior:
                # print('AQUI')
                # print(f'intervalo = {intervalo}')
                return self.pontosMedios[i]

            i += 1

        # Isso não deve acontecer, mas caso não encontre nenhum intervalo
        # retorna o ultimo
        return self.pontosMedios[-1]
