menu = '''
==============================

[0] Deposito
[1] Sacar
[2] Extrato
[s] Sair

==============================

=>'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
Limite_sagues = 3

while True:
    
    opçao = input(menu)

    if opçao == "0":
        valor = float(input("Qual seria o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"

        else:
            print("Aconteceu uma falha, valor não é valido")

    elif opçao == "1":
        valor = float(input("informe o valor a ser sacado: "))

        excedeu_saldo = valor > saldo

        exeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saques
        
        if excedeu_saldo:
            print('Falha, pouco saldo.')

        elif excedeu_limite:
            print('Falha, limite baixo')

        elif excedeu_saques:
            print('Falha, excedeu o nùmero ')

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1

        else:
            print('Falha, Valor inválido')

    elif opçao == "2":
        print('\n===================EXTRATO===================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('===============================================')

    elif opçao == "s":
        break

    else:
        print("Opção de escolha invalida, por favor senlecione novamente.")