# Não permitir valores negativos.
# Limite de 3 saques diários no limite de 500,00 no total.
# Exibir todos os movimentos financeiros.
# os valores devem ser exibidos utilizando formato R$ xxx.xx

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair


"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# VOU MANTER OS MEUS CÓDIGOS QUE ESTAVAM SENDO USANDOS ANTES DE ASSISTIR AO VÍDEO DE RESOLUÇÃO DO DESAFIO.
# Eu estava usando listas e estava tudo funcionando até que eu tive dificuldades em exibir o extrato em ordem de execução.
# lista_deposito = []
# lista_saque = []
# soma_dos_depositos = 0
# soma_dos_saques = 0
# d = 0
# s = 0

while True:

    opcao = input(menu)

    if opcao == "d": # DEPÓSITO
        valor = float(input('Digite o valor do depósito: '))
        if valor > 0:
        #    lista_deposito.append(valor)
        #    print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        #    soma_dos_depositos = sum(lista_deposito)
        #    d += 1
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(extrato)
        else:
            print('Valor inválido')

    elif opcao == "s": # SAQUE
        
        #if s < 3:
        #    valor = float(input('Digite o valor do saque: '))
        #    if valor >= 0 and valor < (soma_dos_depositos - soma_dos_saques) and valor <= limite:
        #        lista_saque.append(valor)
        #        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        #        soma_dos_saques = sum(lista_saque)
        #        s += 1
        #    else:
        #        print('Valor inválido ou insuficiente')
        #else:
        #    print("Quantidade limite de 3 saques atingido, tente novamente amanhã")
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou!  O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            limite -= valor
        
        else:
            print("Operação falhou! O valor informado é inválido!")


    elif opcao == "e":
            print("\n========== EXTRATO ==========")
            #while d != 0:
            #    print(f"Depósito de R$ {lista_deposito[d-1]:.2f}")
            #    d -= 1
            #while s != 0:
            #    print(f"Saque de R$ {lista_saque[s-1]:.2f}")
            #    s -= 1
            #print(f"Saldo remanescente = R$ {(soma_dos_depositos) - (soma_dos_saques):.2f}")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"Saldo: R$ {saldo:.2f}")
            print("=============================")

    elif opcao == "x":
        #lista_deposito = 0
        #lista_saque = 0
        #s = 0
        #d = 0
        break
    else:
        print("Operação inválida, por favor, selecione novamente a operação desejada.")