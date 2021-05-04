class FilaFinita:
    def __init__(self, maxClientes):
        self.fila = []
        self.maxClientes = maxClientes

    def addCliente(self, cliente):
        if len(self.fila) > maxClientes:
            return False

        self.fila.append(cliente)
        return True

    def removeCliente(self):
        if len(self.fila) > 0:
            return self.fila.pop(0)
        
        print('Erro, removendo de uma fila vazia')
        return None

    def vazia(self):
        return len(self.fila) == 0
