# Simulação

## Requisitos

Testado e desenvolvido em ambiente linux

- python3
- pip3
- numpy

Dependências funcionais do programa, como o numpy, podem ser adquiridas com o seguinte comando:

```console
pip3 install -r requirements.txt
```

## Como usar

O usuário pode controlar dois aspectos da simulação:
- Tempo entre chegada de clientes
- Tempo de serviço
- Tamanho da fila

O tempo entre chegada de clientes e tempod e serviço podem ser:
- Determinístico
- Aleatório

O tamanho da fila pode ser:
- Finita
- Infinita

Para tempo entre chegada de clientes, usa-se o parâmetro ```--tipo-fila```, caso aleatório, deve-se informar a base de dados, para determinístico, o tempo, em segundos, entre as chegadas na fila.

Exemplos:
```console
--tipo-fila aleatorio base_fila.txt
--tipo-fila deterministico 3
```

Para tempo de serviço, o mesmo citadoa acima vale, mas com o parâmetro ```--tipo-servico```.

Exemplos:
```console
--tipo-servico aleatorio base_servico.txt
--tipo-servico deterministico 5
```

O tipo de fila deve ser informada pelo parâmetro ```--tam-fila```. Se for finita, deve ser informada o tamanho dela.

Exemplo:
```console
--tam-fila finita 10
--tam-fila infinita
```

## Exemplos de simulações

Tempo de chegada de clientes aleatório, tempo de serviço determinístico de 5 segundos, fila infinita.
```console
python3 main.py --tipo-fila aleatorio base_fila.txt --tipo-servico deterministico 5 --tam-fila infinita
```


Tempo de chegada determinístico de 5 segundos, tempo de serviço aleatório baseado em base_servico.txt, fila finita de 10 lugares
```console
python3 main.py --tipo-fila deterministico 5 --tipo-servico aleatorio base_servico.txt --tam-fila finita 10
```

## Encerrando a Simulação
A simulação é encerrada ao programa receber um sinal de ```KeyboardInterrupt```, no ambiente **Linux**, após ```CTRL-C``` ser pressionado no terminal.

Após isso, algumas estatísticas da simulação serão calculadas e exibidas ao usuário.
