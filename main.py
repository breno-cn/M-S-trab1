from GeradorTempo.GeradorAleatorio import GeradorAleatorio
from GeradorTempo.GeradorDeterministico import GeradorDeterministico
from cliente.Cliente import Cliente
from fila.FilaInfinita import FilaInfinita
from fila.FilaFinita import FilaFinita

import time
import argparse

# TODO: verificar onde por o calculo do tick
#       procurar alguma interface gráfica ou algum print bonitim de terminal
#       alterar parametros
#       testar fila finita e fazer tratamento quando não couber mais clientes nela

# TEMPORÁRIO
def gotoxy(x,y):
    print ("%c[%d;%df" % (0x1B, y, x), end='')

def printTela(totalFila, tempoServico):
    for i in range(10):
        print(' ')

    gotoxy(0, 0)
    print(f'clientes na fila: {totalFila}')
    # print('')
    # print('')
    print(f'tempo de servico restante: {tempoServico}')
    # print('')
    # print('')

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tipo-fila', nargs='*')
    parser.add_argument('--tipo-servico', nargs='*')

    parser.add_argument('--tam-fila', nargs='*')

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
#   python3 main.py --tipo-fila deterministico 3 --tipo-servico deterministico 3 --tam-fila finita 10
#   python3 main.py --tipo-fila aleatorio tempo_chegada_teste.txt --tipo-servico aleatorio tempo_chegada_servico.txt -iFila 3 -iServico 3 --tam-fila infinita


def getGerador(args, tipo):
    tipoGerador = args.tipo_fila[0] if tipo == 'fila' else args.tipo_servico[0]

    if tipoGerador == 'aleatorio':
        intervalos = int(args.iFila) if tipo == 'fila' else int(args.iServico)
        return GeradorAleatorio(args.tipo_fila[1], intervalos) if tipo == 'fila' else GeradorAleatorio(args.tipo_servico[1], int(args.iServico))

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
    tempoProximoServico = 0

    # Variaveis usadas para extrair informações da simulação
    ticks = 0
    totalNumEntidadesFila = 0
    tempoTotalEntidadesFila = 0
    tempoTotalOcupacaoServidores = 0

    gotoxy(0, 0)
    print(' ' * 500)

    while True:
        try:
            if proximaChegada == 0:
                # print('Novo cliente')

                tempoServico = geradorServico.gerarTempo()
                cliente = Cliente(tempoServico)

                if fila.addCliente(cliente):
                    # print(f'cliente {cliente} adicionado com sucesso')
                    totalNumEntidadesFila += 1
                else:
                    print(f'erro ao inserir {cliente} na fila')

                proximaChegada = geradorChegada.gerarTempo()

                # print(cliente)
                # print(fila)

                continue

            if tempoProximoServico == 0 and not fila.vazia():
                ticks += 1

                servido = fila.removeCliente()
                # print(f'servido = {servido}')
                # print('-' * 100)
                # print(servido.tmpEsperaServico)
                # print('-' * 100)
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
            # print(fila)
            # print(tempoProximoServico)
            printTela(len(fila.fila), tempoProximoServico)

        except KeyboardInterrupt:
            gotoxy(0, 5)
            
            print('\n' + '=' * 100)
            print('Encerrando simulacao...')

            print(f'Media de entidades na fila: {totalNumEntidadesFila / ticks}')

            tempoMedioEntidadesFila = tempoTotalEntidadesFila / ticks
            print(f'Tempo medio de espera das entidades na fila: {tempoMedioEntidadesFila}')

            tempoMedioOcupacaoServidores = tempoTotalOcupacaoServidores / ticks
            print(f'Tempo medio de ocupacao dos servidores: {tempoMedioOcupacaoServidores}')

            print(f'Tempo medio no sistema: {tempoMedioEntidadesFila + tempoMedioOcupacaoServidores}')

            return


if __name__ == '__main__':
    main()
