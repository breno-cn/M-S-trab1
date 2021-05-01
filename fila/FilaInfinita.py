class FilaInfinita:
    def __init__(self):
        self.fila = []

    def addCliente(self, cliente):
        self.fila.append(cliente)
        return True

    def removeCliente(self):
        if len(self.fila) > 0:
            return self.fila.pop(0)
        
        print('Erro, removendo de uma fila vazia')
        return None
