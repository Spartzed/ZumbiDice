def receberDadosJogador(i):
    nome = input("Digite o nome do {}º jogador: ".format(i))
    cerebros = 0
    return nome, cerebros


def inserir(Jogadores, i):
    jogador = receberDadosJogador(i)
    Jogadores[jogador[0]] = jogador[1]
    return True


def adicionarCerebro(nomeJogador, Jogadores, diceFaces):
    pontos = Jogadores[nomeJogador]
    if pontos > 0:
        c = pontos
    else:
        c = 0

    for i in diceFaces:
        if i == 'Cerebro':
            c = c + 1
    Jogadores[nomeJogador] = c

    return True


def removerCerebros(nomeJogador, Jogadores):
    c = 0
    Jogadores[nomeJogador] = c
    return True


def scoreAtual(nomeJogador, Jogadores):
    score = Jogadores[nomeJogador]
    return score
