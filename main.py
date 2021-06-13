from GeradorTempo.GeradorAleatorio import GeradorAleatorio
from GeradorTempo.GeradorDeterministico import GeradorDeterministico
from cliente.Cliente import Cliente
from fila.FilaInfinita import FilaInfinita
from fila.FilaFinita import FilaFinita

import time
import argparse

def gotoxy(x,y):
    print ("%c[%d;%df" % (0x1B, y, x), end='')

def printTela(totalFila, tempoServico, proximaChegada):
    for i in range(100):
        print(' ')

    gotoxy(0, 0)
    print(f'clientes na fila: {totalFila}')
    for tempo in tempoServico:
        print(f'tempo de servico restante: {tempo}')
    print(f'tempo para proxima chegada: {proximaChegada}')

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tipo-fila', nargs='*')
    parser.add_argument('--tipo-servico', nargs='*')

    parser.add_argument('--tam-fila', nargs='*')

#   Usados apenas para fila e servico deterministico
    parser.add_argument('--tempo-fila')
    parser.add_argument('--tempo-servico')

    return parser.parse_args()


def getGerador(args, tipo):
    tipoGerador = args.tipo_fila[0] if tipo == 'fila' else args.tipo_servico[0]

    if tipoGerador == 'aleatorio':
        # intervalos = int(args.tipo_fila[0]) if tipo == 'fila' else int(args.tipo_servico[0])
        intervalos = int(args.tipo_fila[2]) if tipo == 'fila' else int(args.tipo_servico[2])
        return GeradorAleatorio(args.tipo_fila[1], intervalos) if tipo == 'fila' else GeradorAleatorio(args.tipo_servico[1], intervalos)

    if tipoGerador == 'deterministico':
        intervalo = int(args.tipo_fila[1]) if tipo == 'fila' else int(args.tipo_servico[1])
        return GeradorDeterministico(intervalo)

def getFila(args):
    tamFila = args.tam_fila[0]
    if tamFila == 'infinita':
        return FilaInfinita()
    
    maxClientes = int(args.tam_fila[1])
    return FilaFinita(maxClientes)

def main():
    args = getArgs()

    geradorChegada = getGerador(args, 'fila')
    geradorServico = getGerador(args, 'servico')

    proximaChegada = geradorChegada.gerarTempo()

    fila = getFila(args)
    temposProximosServicos = [0, 0]

    # Variaveis usadas para extrair informações da simulação
    ticks = 0
    ticksServico = 0
    totalNumEntidadesFila = 0
    tempoTotalEntidadesFila = 0
    tempoTotalOcupacaoServidores = 0

    gotoxy(0, 0)
    print(' ' * 500)

    while True:
        try:
            if proximaChegada == 0:

                tempoServico = geradorServico.gerarTempo()
                cliente = Cliente(tempoServico)

                if fila.addCliente(cliente):
                    totalNumEntidadesFila += 1
                else:
                    print(f'erro ao inserir {cliente} na fila')

                proximaChegada = geradorChegada.gerarTempo()

                continue

            i = 0
            for tempoProximoServico in temposProximosServicos:
                if tempoProximoServico == 0 and not fila.vazia():
                    ticksServico += 1

                    servido = fila.removeCliente()
                    temposProximosServicos[i] = servido.tmpEsperaServico

                    tempoTotalEntidadesFila += servido.tmpEsperaFila

                    tempoTotalOcupacaoServidores += servido.tmpEsperaServico
                i += 1

            for cliente in fila.fila:
                cliente.avancaTempoFila()

            i = 0
            for tempoProximoServico in temposProximosServicos:
                if tempoProximoServico > 0:
                    temposProximosServicos[i] -= 1
                i += 1

            proximaChegada -= 1
            time.sleep(0.1)
            printTela(len(fila.fila), temposProximosServicos, proximaChegada)
            ticks += 1

        except KeyboardInterrupt:
            gotoxy(0, 5)
            
            print('\n' + '=' * 100)
            print('Encerrando simulacao...')

            print(f'Media de entidades na fila: {totalNumEntidadesFila / ticks}')

            tempoMedioEntidadesFila = tempoTotalEntidadesFila / ticks
            print(f'Tempo medio de espera das entidades na fila: {tempoMedioEntidadesFila}')

            tempoMedioOcupacaoServidores = tempoTotalOcupacaoServidores / ticksServico
            print(f'Tempo medio de ocupacao dos servidores: {tempoMedioOcupacaoServidores}')

            print(f'Tempo medio no sistema: {tempoMedioEntidadesFila + tempoMedioOcupacaoServidores}')

            return


if __name__ == '__main__':
    main()
