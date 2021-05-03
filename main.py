from GeradorTempo.GeradorAleatorio import GeradorAleatorio
from GeradorTempo.GeradorDeterministico import GeradorDeterministico
from cliente.Cliente import Cliente
from fila.FilaInfinita import FilaInfinita

import time
import argparse

# TODO: verificar onde por o calculo do tick
#       procurar alguma interface gráfica ou algum print bonitim de terminal
#       alterar parametros

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tipo-fila')
    parser.add_argument('--tipo-servico')

#   Usados apenas para fila e servico deterministico
    parser.add_argument('--tempo-fila')
    parser.add_argument('--tempo-servico')
    # parser.add_argument('--tempo-espera')
    
    
    # args = parser.parse_args()
    # print(args.tipo_fila)
    # print(args.tipo_servico)
    # print(args.tempo_fila)
    # print(args.tempo_servico)

    return parser.parse_args()


# TODO: opções de intervalos nos geradores aleatórios
# Exemplos para rodar o programa: 
#   python3 main.py --tipo-fila aleatorio --tipo-servico aleatorio
#   python3 main.py --tipo-fila deterministico --tempo-fila 2 --tipo-servico deterministico --tempo-servico 1


def main():
    args = getArgs()

    # Declaração de objetos usados na simulação
    geradorChegada = None
    geradorServico = None

    tipo_fila = args.tipo_fila    
    if tipo_fila == 'aleatorio':
        geradorChegada = GeradorAleatorio('tempo_chegada_teste.txt', 3)
    elif tipo_fila == 'deterministico':
        intervalo = int(args.tempo_fila)
        geradorChegada = GeradorDeterministico(intervalo)

    tipo_servico = args.tipo_servico
    if tipo_servico == 'aleatorio':
        geradorServico = GeradorAleatorio('tempo_chegada_servico.txt', 3)
    elif tipo_servico == 'deterministico':
        intervalo = int(args.tempo_servico)
        geradorServico = GeradorDeterministico(intervalo)

    # Teste para gerador Aleatorio
    # geradorChegada = GeradorAleatorio('tempo_chegada_teste.txt', 3)
    # geradorServico = GeradorAleatorio('tempo_chegada_servico.txt', 3)

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
            time.sleep(0.1)
            print(fila)
            print(tempoProximoServico)

        except KeyboardInterrupt:
            print('\n' + '=' * 100)
            print('Encerrando simulacao...')

            print(f'Media de entidades na fila: {totalNumEntidadesFila / ticks}')

            print(f'Tempo medio de espera das entidades na fila: {tempoTotalEntidadesFila / ticks}')

            print(f'Tempo medio de ocupacao dos servidores: {tempoTotalOcupacaoServidores / ticks}')

            print(f'Tempo medio no sistema: {(tempoTotalEntidadesFila / ticks) + (tempoTotalOcupacaoServidores / ticks)}')

            return


if __name__ == '__main__':
    main()
