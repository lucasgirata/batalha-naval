from random import randint
from time import sleep

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
print("Bem-vindo(a) à Batalha Naval! Seu trabalho é destruir as embarcações do inimigo. Para isso,")
sleep(3)
print("Você deverá adivinhar em quais posições elas estão, em linhas de 0 a 4 e colunas de 0 a 9")
sleep(3)
print("As jogadas serão intercaladas, uma vez você tentará adivinhar e na próxima o Computador fará sua jogada.")
sleep(3)
print("Esse é o seu tabuleiro: ")
sleep(1)
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

def posicoesComputador(): #Função para escolher as posições do computador de forma aleatória
    for i in range(5):
        linhaAleatoria = randint(0, 4) #Escolhe linha aleatória entre 0 e 4
        colunhaAleatoria = randint(0, 9) #Escolhe coluna aleatória entre 0 e 9

        tabuleiroComputador[linhaAleatoria][colunhaAleatoria] = "🚢" #Substitui espaço vazio no tabuleiro pela embarcação (🚢)

posicoesComputador() #Chama a função

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

posicoesJogador() #Chama a função
sleep(0.5)
print("\nSuas 5 embarcações foram posicionadas assim!: ") #Mostra como o tabuleiro final do jogador ficou
for i in range(5):
    print(tabuleiroJogador[i])
    sleep(0.1)

print("\nSeu inimigo não sabe onde suas embarcações estão!")
sleep(3)
print("Assim como você, seu inimigo acabou de posicionar sua frota")
sleep(3)
print("Porém, você também não sabe onde ela está!\n")
sleep(3)
print("Agora, vamos dar início ao jogo! Você começa:\n")

for i in range(5):
    print(tabuleiroComputador[i])

def adivinharInimigo():

    contadorNaviosAcertados = 0

    linha = int(input("Tente adivinhar em qual linha (0 a 4) está a embarcação do inimigo: "))
    coluna = int(input("Agora, tente adivinhar em qual coluna (0 a 9) está: "))

    if tabuleiroComputador[linha][coluna] == "🚢":
        contadorNaviosAcertados += 1
        print(f"Boom! Você acertou o {contadorNaviosAcertados}° navio! Restam apenas {5 - contadorNaviosAcertados}")
    elif 

adivinharInimigo()