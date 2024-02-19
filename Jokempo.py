import random

escolha_usuario = int(input("1-Pedra \n2-Papel \n3-Tesoura\n Escolha um número: "))

escolha_PC = random.randint(1, 3)
if (escolha_usuario == escolha_PC):
    print("Você escolheu:", escolha_usuario)
    print("O computador escolheu:", escolha_PC)
    print("Empate")
elif (escolha_usuario == 1 and escolha_PC == 2):
    print("Você escolheu:", escolha_usuario)
    print("O computador escolheu:", escolha_PC)
    print("Você perdeu! :( ")
elif (escolha_usuario == 1 and escolha_PC == 3):
    print("Você escolheu:", escolha_usuario)
    print("O computador escolheu:", escolha_PC)
    print("Você ganhou! :) ")
elif (escolha_usuario == 2 and escolha_PC == 1):
    print("Você escolheu:", escolha_usuario)
    print("O computador escolheu:", escolha_PC)
    print("Você ganhou! :) ")
elif (escolha_usuario == 2 and escolha_PC ==3):
    print("Você escolheu:", escolha_usuario)
    print("O computador escolheu:", escolha_PC)
    print("Você perdeu! :( ")
elif (escolha_usuario == 3 and escolha_PC == 1):
    print("Você escolheu:", escolha_usuario)
    print("O computador escolheu:", escolha_PC)
    print("Você perdeu! :( ")
elif (escolha_usuario == 3 and escolha_PC == 2):
    print("Você escolheu:", escolha_usuario)
    print("O computador escolheu:", escolha_PC)
    print("Você ganhou! :) ")
