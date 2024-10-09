import os

limite_diario = 0
extrato = []
saldo_conta = 0

os.system('cls')

def sacar_valor(saldo_conta):
    saque = float(input("\nQual valor deseja sacar? "))
    
    if saque <= 500 and saque > 0:
        if saldo_conta >= saque:
            os.system('cls')
            print(f"\n***Saque no valor {saque} realizado com sucesso!")
            print("\nObrigada por utilizar nossos serviços, até logo")
            return 1, saque  
        else:
            os.system('cls')
            print("\nSaldo insuficiente para esse saque!")
            return 0, 0  
    if saque < 0:
        os.system('cls')
        print("Valor de saque não pode ser negativo!") 
        return 0, 0
    else:
        os.system('cls')
        print("\nO valor máximo de saque é R$ 500.")
        return 0, 0  
    
def deposito_valor():
    deposito = float(input("\nQual o valor que deseja depositar? "))
    
    if deposito > 0:
        os.system('cls')
        print(f"\n***Valor {deposito} depositado com sucesso!")
        print("\nObrigada por utilizar nossos serviços, até logo!")
        return deposito  
    else:
        os.system('cls')
        print("\n***Valor digitado é inválido para depósito.")
        return 0  

while True:
    
    banco = "\n\nPy Bank"
    print("{:^40}".format(banco))

    opcao = int(input("""\n
    [1] Sacar 
    [2] Deposito 
    [3] Extrato 
    [0] Encerrar
    \nQual opção deseja: """))
    
    if opcao == 1:
        if limite_diario <= 2:
            saque_realizado, saque_valor = sacar_valor(saldo_conta)
            if saque_realizado:
                saldo_conta -= saque_valor
                limite_diario += 1
                extrato.append(-saque_valor)
        else:
            os.system('cls')
            print("\nVocê atingiu o limite de 3 saques diários.")
        continue
          
    elif opcao == 2:
        valor_deposito = deposito_valor()  
        if valor_deposito > 0:  
            extrato.append(valor_deposito)
            saldo_conta += valor_deposito
        continue
    elif opcao == 3:
        os.system('cls')
        print("\nExtrato: ")
        for valor in extrato:
            print("R$ {:.2f}".format(valor))
        print("\nSaldo atual: R$ {:.2f}".format(saldo_conta))
        continue
    elif opcao == 0:
        os.system('cls')
        print("\n--- Sessão encerrada ---\n")
        break
    else:
        os.system('cls')
        print("Opcao invalida, por favor selecione uma opcao valida.")
