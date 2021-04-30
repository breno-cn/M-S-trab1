import pandas as pd

class TECAleatorio:

    # Recebe o caminho para um csv contendo dados iniciais
    # que serão usados para o método Monte Carlo
    def __init__(self, dadosIniciais: str):
        self.data = pd.read_csv(dadosIniciais)

    def gerarTempo():
        pass
