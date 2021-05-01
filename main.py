from GeradorTempo.GeradorAleatorio import *
from cliente.Cliente import Cliente
from fila.FilaInfinita import FilaInfinita

import time

def main():
    geradorChegada = GeradorAleatorio('tempo_chegada_teste.txt', 3)
    geradorFila = GeradorAleatorio('tempo_chegada_teste.txt', 3)
    geradorServico = GeradorAleatorio('tempo_chegada_servico.txt', 2)

    proximaChegada = geradorChegada.gerarTempo()

    fila = FilaInfinita()

    while True:
        try:
            if proximaChegada == 0:
                print('Novo cliente')

                tempoServico = geradorServico.gerarTempo()
                cliente = Cliente(tempoServico)

                fila.addCliente(cliente)

                proximaChegada = geradorChegada.gerarTempo()

                # print(cliente)
                print(fila)
                continue

            for cliente in fila.fila:
                cliente.avancaTempoFila()

            print(f'{proximaChegada} unidades de tempo para proxima chegada')
            proximaChegada -= 1
            time.sleep(0.1)

        except KeyboardInterrupt:
            print('\n' + '=' * 100)
            print('Encerrando simulacao...')
            return


if __name__ == '__main__':
    main()
