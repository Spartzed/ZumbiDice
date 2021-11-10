import random
from players import adicionarCerebro, removerCerebros
import time


def randomDice(Dice, dadosRetirados, repetirDado):
    print("Os dados retirados são: ")
    for v in range(3):
        if Dice != []:
            if len(dadosRetirados) <= 2:
                diceResult = random.choice(Dice)
            else:
                print("Dado(s) Reaprovetitado(s):")
                for dado in repetirDado:
                    print(dado)
                repetirDado = []
                return dadosRetirados, repetirDado
            if diceResult == "Verde":
                Dice.remove('Verde')
                dadosRetirados.append(diceResult)
                print("Verde")
            elif diceResult == "Vermelho":
                Dice.remove('Vermelho')
                dadosRetirados.append(diceResult)
                print("Vermelho")
            elif diceResult == "Amarelo":
                Dice.remove('Amarelo')
                dadosRetirados.append(diceResult)
                print("Amarelo")
        else:
            print("Os dados acabaram")
            repetirDado = False
            return dadosRetirados, repetirDado

    repetirDado = []
    return dadosRetirados, repetirDado


# Gera os resultados dos dados com base na cor dos dados
def randomResult(resultDados, faces, Dice, Jogadores, nomeJogador, dadosRetirados, repetirDado):
    # Receber os dados do dados e atraves disso ver como jogar os dados
    c = Jogadores[nomeJogador]
    f = 0
    t = 0
    Gdice = ['Cerebro', 'Cerebro', 'Cerebro', 'Tiro', 'Fugitivo', 'Fugitivo']
    Ydice = ['Cerebro', 'Cerebro', 'Tiro', 'Tiro', 'Fugitivo', 'Fugitivo']
    Rdice = ['Cerebro', 'Tiro', 'Tiro', 'Tiro', 'Fugitivo', 'Fugitivo']
    for i in resultDados:
        if i == 'Verde':
            g = random.choice(Gdice)
            faces.append(g)
            if g == 'Fugitivo':
                repetirDado.append('Verde')
            print(g)
        elif i == 'Amarelo':
            y = random.choice(Ydice)
            faces.append(y)
            if y == 'Fugitivo':
                repetirDado.append('Amarelo')
            print(y)
        elif i == 'Vermelho':
            r = random.choice(Rdice)
            faces.append(r)
            if r == 'Fugitivo':
                repetirDado.append('Vermelho')
            print(r)
        time.sleep(1)
    # Validar se o jogador levou 3 tiros ou teve 13 pontos
    for i in faces:
        if i == 'Cerebro':
            c = c + 1
            # valida se o jogador fez a quantidade de pontos suficiente
            if c >= 13:
                c = 'WINNER'
                return c
        elif i == 'Passos':
            f = f + 1

        elif i == 'Tiro':
            t = t + 1
            # valida se o jogador levou 3 tiros, se sim mando o comando para passar ao proximo jogador
            if t >= 3:
                removerCerebros(nomeJogador, Jogadores)
                print("Você foi baleado 3 vezes e perdeu todos os pontos")
                t = 'LOSER'
                return t

    return faces


# Define o resultado de cada partida
def resultRound(diceFaces, nomeJogador, Jogadores):
    c = 0
    f = 0
    t = 0
    geral = Jogadores[nomeJogador]
    for i in diceFaces:
        if i == 'Cerebro':
            c = c + 1
        elif i == 'Fugitivo':
            f = f + 1
        elif i == 'Tiro':
            t = t + 1
    print("O seu resultado nessa partida foi de: \n", c, " Cerebros\n", f, " Fugitivos\n", t,
          " Tiros\n""Pontuação Geral :", geral, "Cérebro(s)")
