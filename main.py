from GeradorTempo.GeradorAleatorio import GeradorAleatorio
from GeradorTempo.GeradorDeterministico import GeradorDeterministico
from cliente.Cliente import Cliente
from fila.FilaInfinita import FilaInfinita

import time

def main():
    # Teste para gerador Aleatorio
    geradorChegada = GeradorAleatorio('tempo_chegada_teste.txt', 3)
    geradorServico = GeradorAleatorio('tempo_chegada_servico.txt', 3)

    # Teste para gerador Deterministico
    # geradorChegada = GeradorDeterministico(3)
    # geradorServico = GeradorDeterministico(2)

    proximaChegada = geradorChegada.gerarTempo()

    fila = FilaInfinita()
    tempoProximoServico = 0

    # Variaveis usadas para extrair informações da simulação
    ticks = 0
    totalNumEntidadesFila = 0
    tempoTotalEntidadesFila = 0
    tempoTotalOcupacaoServidores = 0

    while True:
        try:
            if proximaChegada == 0:
                print('Novo cliente')

                tempoServico = geradorServico.gerarTempo()
                cliente = Cliente(tempoServico)

                fila.addCliente(cliente)

                proximaChegada = geradorChegada.gerarTempo()

                print(cliente)
                print(fila)

                totalNumEntidadesFila += 1
                continue

            if tempoProximoServico == 0 and not fila.vazia():
                ticks += 1

                servido = fila.removeCliente()
                print(f'servido = {servido}')
                tempoProximoServico = servido.tmpEsperaServico

                tempoTotalEntidadesFila += servido.tmpEsperaFila

                tempoTotalOcupacaoServidores += servido.tmpEsperaServico

            for cliente in fila.fila:
                cliente.avancaTempoFila()

            if tempoProximoServico > 0:
                tempoProximoServico -= 1

            # print(f'{proximaChegada} unidades de tempo para proxima chegada')
            # print(f'tempoProximoServico = {tempoProximoServico}')
            proximaChegada -= 1
            time.sleep(0.001)
            print(fila)
            print(tempoProximoServico)

        except KeyboardInterrupt:
            print('\n' + '=' * 100)
            print('Encerrando simulacao...')

            print(f'Media de entidades na fila: {totalNumEntidadesFila / ticks}')

            print(f'Tempo medio de espera das entidades na fila: {tempoTotalEntidadesFila / ticks}')

            print(f'Tempo medio de ocupacao dos servidores: {tempoTotalOcupacaoServidores / ticks}')

            return


if __name__ == '__main__':
    main()
