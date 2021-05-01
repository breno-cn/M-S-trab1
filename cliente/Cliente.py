class Cliente:
    def __init__(self, tmpEsperaFila, tmpEsperaServico):
        self.tmpEsperaFila = tmpEsperaFila
        self.tmpEsperaServico = tmpEsperaServico

    def avancaTempoFila(self):
        self.tmpEsperaFila -= 1

    def avancaTempoServico(self):
        self.tmpEsperaServico -= 1

    def __str__(self):
        return f'(tmpEsperaFila = {self.tmpEsperaFila}, tmpEsperaServico = {self.tmpEsperaServico})'
