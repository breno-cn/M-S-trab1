from TEC.TECAleatorio import *

def main():
    TEC = TECAleatorio('tempo_chegada_teste.txt', 2)
    temp1 = TEC.gerarTempo()
    temp2 = TEC.gerarTempo()
    temp3 = TEC.gerarTempo()
    temp4 = TEC.gerarTempo()

    print(temp1)
    print(temp2)
    print(temp3)
    print(temp4)


if __name__ == '__main__':
    main()
