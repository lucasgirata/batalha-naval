#BIBLIOTECAS

from random import randint #Para escolher as posições de forma aleatória
from time import sleep #Para dar pausa entre os prints para maior fluidez



#TABULEIROS

tabuleiroJogador = [ #Tabuleiro 5x10 do Jogador vazio
    ['🟦'] * 10,
    ['🟦'] * 10,
    ['🟦'] * 10,
    ['🟦'] * 10,
    ['🟦'] * 10
    ]

tabuleiroComputador = [ #Tabuleiro 5x10 do Computador vazio
    ['🟦'] * 10,
    ['🟦'] * 10,
    ['🟦'] * 10,
    ['🟦'] * 10,
    ['🟦'] * 10
    ]

tabuleiroPalpitesComputador = [ #Tabuleiro oculto 5x10 do computador que é mostrado ao usuário após fazer sua jogada
    ['🟦'] * 10,
    ['🟦'] * 10,
    ['🟦'] * 10,
    ['🟦'] * 10,
    ['🟦'] * 10
]

tabuleiroPalpitesJogador = [ #Tabuleiro oculto 5x10 do jogador que é mostrado após fazer a jogada
    ['🟦'] * 10,
    ['🟦'] * 10,
    ['🟦'] * 10,
    ['🟦'] * 10,
    ['🟦'] * 10
]



#CONTADORES DE NAVIOS RESTANTES

contadorNaviosRestantesJogador = 5 #Contador de navios restantes do jogador
contadorNaviosRestantesInimigos = 5 #Contador de navios restantes do computador



#FUNÇÕES

def mostrarTabuleiros(tabuleiroPalpitesComputador, tabuleiroPalpitesJogador): #Função para mostrar o tabuleiro oculto do inimigo e o tabuleiro do usuário
    print("\nTabuleiro do inimigo:\n")
    for i in range(5): #Mostra o tabuleiro linha por linha
        print(tabuleiroPalpitesComputador[i])
        sleep(0.1)
    print()
    print("=======================================================")
    print("\nSeu tabuleiro:")
    for i in range(5): #Mostra o tabuleiro linha por linha
        print(tabuleiroPalpitesJogador[i])
        sleep(0.1)

def posicoesComputador(): #Função para escolher as posições do computador de forma aleatória
    for i in range(5):
        linhaAleatoria = randint(0, 4) #Escolhe linha aleatória entre 0 e 4
        colunhaAleatoria = randint(0, 9) #Escolhe coluna aleatória entre 0 e 9

        tabuleiroComputador[linhaAleatoria][colunhaAleatoria] = "🚢" #Substitui espaço vazio no tabuleiro pela embarcação (🚢)

def posicoesJogador(): #Função para o jogador escolher em quais posições as embarcações serão colocadas

        embarcacoesPosicionadas = 0 #Contador de embarcações já colocadas

        while embarcacoesPosicionadas != 5: #Enquanto o contador não for 5

            print("\nSeu tabuleiro: ") #Mostra como o tabuleiro está
            for i in range(5):
                print(tabuleiroJogador[i])
                sleep(0.1)

            linhaJogador = int(input("\nEscolha em qual linha (0 a 4) a embarcação será posicionada: ")) #Pergunta em qual linha será colocado

            if linhaJogador >= 0 and linhaJogador <=4: #Condicional para que o valor de linha inserido seja valido

                colunaJogador = int(input("\nEscolha em qual colunha (0 a 9) a embarcação será posicionada: ")) #Pergunta em qual coluna será posicionado

                if colunaJogador >= 0 and colunaJogador <= 9: #Condicional para que o valor de coluna inserido seja validod

                    tabuleiroJogador[linhaJogador][colunaJogador] = "🚢" #Substitui a posição da "casa" vazia pelo návio
                    embarcacoesPosicionadas += 1 #Adiciona mais um ao contador de embarcações

                else: #Condicional caso o valor de coluna seja inválido
                    print("\nValor inválido! Tente novamente")

            else: #Condicional caso o valor de linha seja inválido
                print("\nValor inválido! Tente novamente")

def adivinharInimigo(contadorNaviosRestantesInimigo): #Função para o jogador tentar adivinhar a coordenada das embarcações inimigas

    mostrarTabuleiros(tabuleiroPalpitesComputador,tabuleiroPalpitesJogador) #Chama a função dos dois tabuleiros ocultos

    linha = int(input("\nTente adivinhar em qual linha (0 a 4) está a embarcação do inimigo: ")) #Input para linha

    if linha >= 0 and linha <= 4:

        coluna = int(input("Agora, tente adivinhar em qual coluna (0 a 9) está: ")) #Input para coluna

        if coluna >= 0 and coluna <= 9:

            sleep(2)

            if tabuleiroComputador[linha][coluna] == "🚢": #Se a string da posição escolhida for um ícone de navio

                contadorNaviosRestantesInimigo -= 1 #Contador de navios do inimigo subtrai 1
                print(f"\nBoom! Você acertou um navio! Restam apenas {contadorNaviosRestantesInimigo} dele") #Mostra quantos restam
                tabuleiroPalpitesComputador[linha][coluna] = "💥" #Substitui o ícone por um de explosão
                tabuleiroComputador[linha][coluna] = "💥"
                sleep(2)

            elif tabuleiroComputador[linha][coluna] == "🟦": #Ou, se a string for um espaço em branco

                print(f"\nErrou! Tente no próximo turno. Ainda restam {contadorNaviosRestantesInimigo} dele") #Mostra que errou e quantos restam
                tabuleiroPalpitesComputador[linha][coluna] = "✖️" #Substitui por um ícone para indicar que aquele local já foi escolhido
                tabuleiroComputador[linha][coluna] = "✖️" #Substitui por um ícone para indicar que aquele local já foi escolhido
                sleep(2)

            elif tabuleiroComputador[linha][coluna] == "✖️" or tabuleiroComputador[linha][coluna] == "💥":

                print(f"\nVocê tentou acertar uma posição onde já atirou, logo, perdeu a vez! Ainda restam {contadorNaviosRestantesInimigos} dele")
                sleep(2)

            else:  # Condicional caso o valor de coluna seja inválido
                print("\nValor inválido! Tente novamente")

            return contadorNaviosRestantesInimigo #Retorna o contador de navios que restam do inimigo

        else:

            sleep(2)

            print("\nValor inválido! Você perdeu sua vez")

            sleep(2)

    else:

        sleep(2)

        print("\nValor inválido! Você perdeu sua vez")

        sleep(2)

def adivinharComputador(contadorNaviosRestantesJogador): #Função para o computador tentar adivinhar as coordenadas do inimigo

    mostrarTabuleiros(tabuleiroPalpitesComputador, tabuleiroPalpitesJogador) #Chama a função de mostrar os dois tabuleiros ocultos

    linhaPC = randint(0, 4) #Randomiza o número da linha do tabuleiro
    print(f"\nSeu inimigo escolheu a linha {linhaPC}")

    sleep(1)

    colunaPC = randint(0, 9) #Randomiza o número da coluna do tabuleiro
    print(f"E a colunha {colunaPC}")

    sleep(3)

    if tabuleiroJogador[linhaPC][colunaPC] == "🚢": #Se na coordenada escolhida, a string for um navio
        tabuleiroPalpitesJogador[linhaPC][colunaPC] = "💥" #Substitui pela explosão
        tabuleiroJogador[linhaPC][colunaPC] = "💥" #Substitui pela explosão
        contadorNaviosRestantesJogador -= 1 #Subtrai um do contador
        print(f"\nO inimigo acertou seu navio! Restam apenas {contadorNaviosRestantesJogador} seus") #Informa que foi acertado e quantos restam
        sleep(2)

    elif tabuleiroJogador[linhaPC][colunaPC] == "🟦": #Ou, se na coordenada escolhida, a string for um espaço em branco
        print(f"\nO inimigo errou seu navio! Ainda restam {contadorNaviosRestantesJogador} seus") #Informa que errou e quantos restam
        tabuleiroPalpitesJogador[linhaPC][colunaPC] = "✖️" #Substitui pelo ícone de erro
        tabuleiroJogador[linhaPC][colunaPC] = "✖️" #Substitui pelo ícone de erro
        sleep(2)

    elif tabuleiroJogador[linhaPC][colunaPC] == "✖️" or tabuleiroJogador[linhaPC][colunaPC] == "💥": #Ou,se a coordenada já foi tentada antes
        print(f"\nO inimigo tentou acertar onde já atirou e perdeu sua vez! Ainda restam {contadorNaviosRestantesJogador} seus") #Informa que perdeu a vez e quantos restam
        sleep(2)

    return contadorNaviosRestantesJogador #Retorna o contador de navios do jogador



#FLUXO DO JOGO

print("========== BATALHA NAVAL ==========\n")
print("             |    |    |")
print("            )_)  )_)  )_)")
print("           )___))___))___)\\")
print("          )____)____)_____)\\\\")
print("        _____|____|____|____\\\\\\__")
print("---------\\              /---------")
print("  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^")
print("    ^^^^              ^^^^")
print("         ^^^^      ^^^^\n")
print("====================================\n")
sleep(1)
print("Bem-vindo(a) à Batalha Naval! Seu trabalho é destruir as embarcações do inimigo. Para isso,") #Explica regras básicas
sleep(3)
print("Você deverá adivinhar em quais posições elas estão, em linhas de 0 a 4 e colunas de 0 a 9.")
sleep(3)
print("As jogadas serão intercaladas, uma vez você tentará adivinhar e na próxima o Computador fará sua jogada.")
sleep(3)
print("Esse é o seu tabuleiro: ")
sleep(1)

posicoesJogador() #Chama a função para o usuário escolher onde os návios vão ser posicionados

sleep(0.5)

print("\nSuas 5 embarcações foram posicionadas assim!: ") #Mostra como o tabuleiro final do jogador ficou, linha por linha
for i in range(5):
    print(tabuleiroJogador[i])
    sleep(0.1)

posicoesComputador() #Chama a função para o computador escolher onde os návios vão ser posicionados

print("\nAssim como você, seu inimigo acabou de posicionar sua frota.") #Explicação das regras do jogo
sleep(3)
print("\nEle não sabe onde suas embarcações estão!")
sleep(3)
print("\nPorém, você também não sabe onde estão as dele!\n")
sleep(3)
print("Agora, vamos dar início ao jogo! Você começa:\n")

while contadorNaviosRestantesJogador != 0 and contadorNaviosRestantesInimigos != 0: #Loop para rodar o jogo enquanto nenhum dos dois ganharem

    contadorNaviosRestantesInimigos = adivinharInimigo(contadorNaviosRestantesInimigos) #Chama a função e faz com que o contador receba o valor que a função retorna, ou seja, se é menos um ou nada

    if contadorNaviosRestantesInimigos == 0: #Se o contador de navios do computador zerar, o loop do while se encerra e o jogador ganha
        break

    contadorNaviosRestantesJogador = adivinharComputador(contadorNaviosRestantesJogador) #Igual ao semelhante em cima, porém com a jogada do computador

if contadorNaviosRestantesInimigos == 0: #Condicional caso o jogador ganhe
    print("\nPARABÉNS! Você derrotou todos os navios inimigos!")
elif contadorNaviosRestantesJogador == 0: #Condicional caso o computador ganhe
    print("\nFIM DE JOGO! O inimigo derrotou toda sua frota e ganhou o jogo.")

print("\nMuito obrigado por ter jogado!")
print("Desenvolvido por: Lucas Girata, João Esperança, Andrey Brawerman, Equipe 5")
