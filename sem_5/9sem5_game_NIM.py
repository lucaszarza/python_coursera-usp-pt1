def computador_escolhe_jogada(n, m):
    computador_remove = 1

    while computador_remove != m:
        if (n - computador_remove) % (m + 1) == 0:
            return computador_remove
        else:
            computador_remove += 1

        return computador_remove


def usuario_escolhe_jogada(n, m):
    jogada_validada = False

    while not jogada_validada:
        jogador_remove = int(input("Quantas peças você vai tirar? "))
        if jogador_remove > m or jogador_remove < 1:
            print("")
            print("Oops! Jogada inválida! Tente de novo.")
            print("")

        else:
            jogada_validada = True

    return jogador_remove


def partida():
    vez_pc = False

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    if n % (m + 1) == 0:
        print()
        print("Você começa!")
    else:
        print()
        print("Computador começa")
        vez_pc = True

    while n > 0:
        if vez_pc:
            computador_remove = computador_escolhe_jogada(n, m)
            n = n - computador_remove

            if computador_remove == 1:
                print()
                print("O computador tirou uma peçca")
            else:
                print()
                print(f"O computador tirou {computador_remove} peças")

            vez_pc = False
        else:
            jogador_remove = usuario_escolhe_jogada(n, m)
            n = n - jogador_remove
            if jogador_remove == 1:
                print()
                print("Você tirou uma peça")
            else:
                print()
                print(f"Você tirou {jogador_remove} peças")
            vez_pc = True
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.")
            print()
        else:
            if n != 0:
                print(f"Agora restam {n} peças no tabuleiro.")
                print()

        print("Fim do jogo! O computador ganhou!")


def campeonato():
    numero_rodadas = 1

    while numero_rodadas < 4:
        print()
        print(f"**** Rodada {numero_rodadas} ****")
        print()
        partida()
        numero_rodadas += 1
    print()
    print("Placar: Você 0 X 3 Computador")


def main():

    print("Bem-vindo ao jogo do NIM! Escolha:")

    start = int(
        input("1 - para jogar uma partida isolada \n 2 - para jogar um campeonato 2")
    )

    if start == 1:
        print("Você escolheu uma partida isolada!")
        partida()
    elif start == 2:
        print("Você escolheu um campeonato!")
        campeonato()
