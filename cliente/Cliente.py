class Cliente:
    def __init__(self, tmpEsperaFila, tmpEsperaServico=0):
        self.tmpEsperaFila = tmpEsperaFila
        self.tmpEsperaServico = tmpEsperaServico

    def avancaTempoFila(self):
        self.tmpEsperaFila -= 1

    def avancaTempoServico(self):
        self.tmpEsperaServico -= 1
