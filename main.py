from GeradorTempo.GeradorAleatorio import *

def main():
    gerador = GeradorAleatorio('tempo_chegada_teste.txt', 2)
    temp1 = gerador.gerarTempo()
    temp2 = gerador.gerarTempo()
    temp3 = gerador.gerarTempo()
    temp4 = gerador.gerarTempo()

    print(temp1)
    print(temp2)
    print(temp3)
    print(temp4)


if __name__ == '__main__':
    main()
