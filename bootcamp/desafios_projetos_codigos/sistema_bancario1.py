extrato = []
saldo = 0.0
limite_saque = 3 
limite_diario = 500.0
usuarios = []
contas = []
numero_conta = 0
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

def criar_user():
    global contas
    usuario = dict.fromkeys(["nome","dt_nasc","cpf","end"])
    usuario["nome"] = input("informe o nome completo: ")
    usuario["dt_nasc"] = input("informe a data de nascimento: ")
    usuario["cpf"] = input("informe o cpf: ")
    usuario["end"] = input("informe o endereco: ")
    if usuario["cpf"] in usuarios:
        print("usuario ja cadastrado!")
    else:
        usuarios.append(usuario["cpf"])    
def criar_cc():
    global usuarios
    global numero_conta
    usuario = dict.fromkeys(["cpf"])
    usuario["cpf"] = input("informe o cpf: ")
    if usuario["cpf"] not in usuarios:
        print("usuario nao existe!")
    else:
        contas.append({"cpf":usuario["cpf"],"nr_conta":numero_conta + 1,"agencia":"0001" })
        numero_conta = numero_conta + 1 
def menu():
    menu = """########### MENU #############
# 1 - Deposito	             #
# 2 - Saque                  #
# 3 - Extrato                #
# 4 - Criar Usuario          #
# 5 - Criar Conta Corrente   #
############################## """
    print(menu)
    resposta_input = int(input("informe sua operacao: "))
    resposta = int(resposta_input) 

    while resposta  in [1,2,3,4,5]:
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
        elif resposta == 4:
            print("Voce escolheu Criar usuario")            
            criar_user()
            print(usuarios)
        elif resposta == 5:
            print("Voce escolheu Criar Conta Corrente")
            criar_cc()
            print(contas)
        print(menu)
        resposta_input = input("selecione outra operacao: ")
        resposta = int(resposta_input) 
    print("obrigado por usar nosso sistema!!")
    print("####################")


menu()