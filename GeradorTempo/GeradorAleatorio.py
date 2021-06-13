import numpy as np

class GeradorAleatorio:

    def __init__(self, B, intervalos, n):
        self.dadosIniciais = []
        self.dadosIniciaisIntervalados = []
        self.intervalos = intervalos
        self.pontosMedios = []
        self.menor = 0
        self.maior = 0

        distribuicao = np.random.exponential(scale=B, size=n)
        self.dadosIniciais = np.array(list(map(int, distribuicao)))
        self.dadosIniciais.sort()
        self.dadosIniciaisIntervalados = np.array_split(self.dadosIniciais, intervalos)

        self.pontosMedios = [int(intervalo.mean()) for intervalo in self.dadosIniciaisIntervalados]

        self.menor = self.dadosIniciais[0]
        self.maior = self.dadosIniciais[-1]

        print(self.dadosIniciais)
        print(self.pontosMedios)
        print(self.dadosIniciaisIntervalados)


    def gerarTempo(self):
        # Gerar um numero aleatorio
        num = np.random.randint(low=self.menor, high=self.maior, size=1)[0]

        # Verificar qual intervalo esse número pertence
        i = 0
        for intervalo in self.dadosIniciaisIntervalados:
            menor = intervalo[0]
            maior = intervalo[-1]

            # intervalo encontrado
            if num >= menor and num <= maior:
                return self.pontosMedios[i]

            i += 1

        # Isso não deve acontecer, mas caso não encontre nenhum intervalo
        # retorna o ultimo
        return self.pontosMedios[-1]
