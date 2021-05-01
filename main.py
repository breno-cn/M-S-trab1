from GeradorTempo.GeradorAleatorio import *

def main():
    print('=' * 100)
    print('Teste tempo de chegada')

    geradorChegada = GeradorAleatorio('tempo_chegada_teste.txt', 3)
    temp1 = geradorChegada.gerarTempo()
    temp2 = geradorChegada.gerarTempo()
    temp3 = geradorChegada.gerarTempo()
    temp4 = geradorChegada.gerarTempo()

    print(temp1)
    print(temp2)
    print(temp3)
    print(temp4)

    print('=' * 100)
    print('Teste tempo de servico')

    geradorServico = GeradorAleatorio('tempo_chegada_servico.txt', 2)
    temp1 = geradorServico.gerarTempo()
    temp2 = geradorServico.gerarTempo()
    temp3 = geradorServico.gerarTempo()
    temp4 = geradorServico.gerarTempo()

    print(temp1)
    print(temp2)
    print(temp3)
    print(temp4)

if __name__ == '__main__':
    main()
