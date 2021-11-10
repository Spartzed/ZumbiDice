from players import inserir, adicionarCerebro, removerCerebros, scoreAtual
from Dados import randomDice, randomResult, resultRound
import time

# Definição das variaveis usadas durante o jogo
facesroud = []
faces = []
dadosRetirados = []
repetirDado = []
Dice = ['Verde', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde', 'Vermelho', 'Vermelho', 'Vermelho', 'Amarelo', 'Amarelo',
        'Amarelo', 'Amarelo']
manterJogo = True


# Menu chamado ao iniciar o jogo
def menu():
    print("\n", 30 * '-', "Bem-Vindo ao Zumbi Dice", 30 * '-', "\n")
    print("O objetivo do jogo é conseguir 13 Cérebros primeiro, quem o fizer primeiro ganha o jogo\n"
          "Mas Atenção aos tiros em cada rodada, ao receber 3 tiros você perde todos os seus Pontos\n"
          "Regras:\n"
          "1 - Permitido até 5 jogadores\n"
          "2 - Quem fizer 13 Pontos primeiro ganha\n"
          "3 - Ao levar 3 tiros em uma rodada os pontos são zerados\n"
          "4 - São 13 dados por turno, acabando os dados da caixa a rodada acaba e passa ao próximo\n"
          "5 - Caso o Dado caia com  a face 'Fugitivo' o mesmo dado poderá ser lançado novamente\n")


# Identificador de nova partida
def novoRound():
    print(30 * '-', "Proximo turno", 30 * '-')


# Definição da variavel jogadores e definir quantidade de jogadores
Jogadores = {}
menu()
while True:
    try:
        qntdJogadores = int(input("Para começar, digite a quantidade de jogadores: "))
        if qntdJogadores < 2:
            print("Numero de jogadores invalido")
        elif qntdJogadores > 5:
            print("Numero maximo de jogadores atingido, o limite e 5!")
        else:
            break
    except ValueError:
        print("Favor Digitar um numero valido.")

# Insere em um dicionario todos os jogadores
for i in range(1, qntdJogadores + 1):
    inserir(Jogadores, i)

# Inicio do jogo
while manterJogo:

    for nomeJogador in Jogadores:
        # Mostra os dados do jogador e reinicia as variaveis antes de iniciar um novo turno
        scoreJogador = scoreAtual(nomeJogador, Jogadores)
        novoRound()
        print("Sua vez {}!\n""Sua pontuação atual é de {} Cérebros".format(nomeJogador, scoreJogador))
        faces = []
        dadosRetirados = []
        repetirDado = []
        c = 0
        f = 0
        t = 0
        Dice = ['Verde', 'Verde', 'Verde', 'Verde', 'Verde', 'Verde', 'Vermelho', 'Vermelho', 'Vermelho', 'Amarelo',
                'Amarelo', 'Amarelo', 'Amarelo']
        # As rodadas Se mantem dentro desse While
        while True:
            try:
                quantDados = len(Dice)
                print("A quantidade de dados na caixa é: ", quantDados)
                # Vai sortear os dados dentro da função, já printando o resultado
                resultDados = randomDice(Dice, dadosRetirados, repetirDado)
                # Caso retorne false o repetirDado é que acabou os dados da caixinha e pula para proxima rodada
                if repetirDado == False:
                    break
                # Pega o segundo retorno da função resultDados é verifica se tem dados a serem reaproveitados
                repetirDado = resultDados[1]
                print(32 * '-', "Resultado", 32 * '-', )
                # Pega as faces sorteadas
                diceFaces = randomResult(resultDados[0], faces, Dice, Jogadores, nomeJogador, dadosRetirados,
                                         repetirDado)
                # Valida se o jogador fez 13 pontos
                if diceFaces == 'WINNER':
                    print("Parabéns {} você foi o ganhador da partida".format(nomeJogador))
                    time.sleep(100)
                    exit()
                # verifica se o jogador levou 3 tiros e perdeu todos os pontos, passando pra proxima rodada
                if diceFaces == 'LOSER':
                    break
                # Caso o jogador não queira jogador novamente pula para proxima rodada
                if input("-----Deseja Jogar novamente?  S/N ----- ").strip().upper()[0] == 'N':
                    adicionarCerebro(nomeJogador, Jogadores, diceFaces)
                    resultRound(diceFaces, nomeJogador, Jogadores)
                    break
                dadosRetirados = []
                # Verifica se a caixa de dados está vazia, se não ele adiciona os dados
                # a serem reaproveitado aos que serão lançados na proxima rodada
                if Dice != []:
                    dadosRetirados.extend(repetirDado)
                else:
                    print("Todos os dados foram retirados da caixa!!")
                    break
            except ValueError:
                print("Tente Digitar novamente")
