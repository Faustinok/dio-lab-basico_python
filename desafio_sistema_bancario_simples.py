menu = """####### MENU #######
# 1 - Deposito	   #
# 2 - Saque        #
# 3 - Extrato      #
#################### """
extrato = []
saldo = 0.0
limite_saque = 3 
limite_diario = 500.0

print (menu)
def deposito():
    global saldo
    valor_deposito1= input("Informe: o valor do Deposito positivo: ")
    valor_deposito =float(valor_deposito1)
    valor_deposito= verifica_valor_negativo(valor_deposito)
    saldo = saldo +  valor_deposito

    extrato.append(f"Deposito de R${valor_deposito: .2f} ")
def saque():
    global limite_diario
    global saldo
    global limite_saque
    if verifica_saque():
        print("Voce passou dos limites diarios de saque ou do valor diario de saque!!")
    else:
        valor_saque1= input("Informe o valor positivo que deseja sacar: ")
        valor_saque =float(valor_saque1)
        if verifica_valor_negativo(valor_saque):
            while limite_diario - valor_saque < 0:
                print("Valor diario de saque ultrapassado!")
                valor_saque= input("Informe outro valor menor de saque positivo: ")
                valor_saque =float(valor_saque)
            limite_saque = limite_saque -  1 
            print("valor novo do limite_saque: {sd}".format(sd =limite_saque ))
            limite_diario = limite_diario - valor_saque
            saldo = saldo - valor_saque
            extrato.append(f"Saque de R${valor_saque: .2f}")         


def verifica_saque():
    return limite_diario  <= 0 or limite_saque <= 0 or saldo < 0
def verifica_valor_negativo(valor):
    while valor < 0:
        print("valor precisa ser maior que zero!")
        valor= input("Informe o valor novamente: ")
        return float(valor)
    return valor
resposta_input = int(input("informe sua operacao: "))
resposta = int(resposta_input) 

while resposta  in [1,2,3]:
    if resposta == 1:
        print("Voce escolheu Deposito")
        deposito()
    elif resposta == 2:
        print("Voce escolheu Saque")
        saque()
    elif resposta == 3:
        print("Voce escolheu Extrato")
        print("")
        for transacao in extrato:            
            print(transacao)        
    print (menu)
    resposta_input = input("selecione outra operacao: ")
    resposta = int(resposta_input) 
print("obrigado por usar nosso sistema!!")
print("####################")
