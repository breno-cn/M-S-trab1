class FilaFinita:
    def __init__(self, max):
        self.fila = []
        self.max = max

    def addCliente(self, cliente):
        if len(self.fila) > max:
            return False

        self.fila.append(cliente)
        return True

    def removeCliente(self):
        if len(self.fila) > 0:
            return self.fila.pop(0)
        
        print('Erro, removendo de uma fila vazia')
        return None