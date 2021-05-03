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
    parser.add_argument('--tipo-fila', nargs='*')
    parser.add_argument('--tipo-servico', nargs='*')

#   Usados apenas para fila e servico aleatorio
    parser.add_argument('-iFila')
    parser.add_argument('-iServico')
    # 
    # parser.add_argument('--base-fila')
    # parser.add_argument('--base-servico')

#   Usados apenas para fila e servico deterministico
    parser.add_argument('--tempo-fila')
    parser.add_argument('--tempo-servico')

    return parser.parse_args()


# TODO: opções de intervalos nos geradores aleatórios
# Exemplos para rodar o programa: 
#   python3 main.py --tipo-fila aleatorio --tipo-servico aleatorio
#   python3 main.py --tipo-fila aleatorio --tipo-servico aleatorio -iFila 3 -iServico 3


def getGerador(args, tipo):
    tipoGerador = args.tipo_fila[0] if tipo == 'fila' else args.tipo_servico[0]

    if tipoGerador == 'aleatorio':
        intervalos = int(args.iFila) if tipo == 'fila' else int(args.iServico)
        return GeradorAleatorio(args.tipo_fila[1], intervalos) if tipo == 'fila' else GeradorAleatorio(args.tipo_servico[1], int(args.iServico))

    if tipo == 'deterministico':
        intervalo = int(args.tempo_fila) if tipo == 'fila' else int(args.tempo_servico)
        return GeradorDeterministico(intervalo)

def main():
    args = getArgs()

    geradorChegada = getGerador(args, 'fila')
    geradorServico = getGerador(args, 'servico')

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
