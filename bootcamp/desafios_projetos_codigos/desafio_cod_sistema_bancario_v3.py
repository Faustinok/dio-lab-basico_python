import textwrap
from abc import ABC,abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self,endereco):
        self.endereco = endereco
        self.contas =[]
    def realizar_transacao(self,conta,transacao):
        transacao.registrar(conta)
    
    def adicionar_conta(self,conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome,data_nasc,cpf,endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nasc = data_nasc
        self.cpf = cpf

class Conta:
    def  __init__(self,numero,cliente):
        self._saldo = 0 
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls,cliente,numero):
        return cls(numero,cliente)
    
    @property
    def saldo(self):
        return self._saldo
    @property
    def numero(self):
        return self._numero
    @property
    def agencia(self):
        return self._agencia
    
    @property 
    def cliente(self):
        return self._cliente
    @property
    def historico(self):
        return self._historico
    
    def sacar(self,valor):
        saldo = self._saldo
        excedeu_saldo = valor < saldo

        if excedeu_saldo:
            print("")
            print("@@@ Operacao falhou! voce nao tem saldo suficiente. @@@")
        elif valor > 0 :
            self._saldo -= saldo
            print("")
            print(" Saque realizado com sucesso!")
            return True
        else:
            print("")
            print("O valor informado e invalido")
        return False
    def depositar(self,valor):
        if valor > 0:
            self._saldo += valor
            print("")
            print(" Saque realizado com sucesso!")
            return True
        else:
            print("")
            print("O valor informado e invalido")
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente,limite =500,limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
    def sacar(self,valor):
        numero_saques = len(transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__)

        excedeu_limite = valor > self.limite
        excedeu_saque = numero_saques > self.limite_saques
        
        if excedeu_limite:
            print("")
            print("O valor do saque excedeu o limite!")
        elif excedeu_saque:
            print("")
            print("Numero maximo de saques excedido")
        else:
            return super().sacar(valor)
        return False

class Historico:
    def __init__(self):
        self._transacoes =[]
    def adicionar_transacao(self,transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    @abstractmethod
    def registrar(self,conta):
        PessoaFisica
class Saque(Transacao):
    def __init__(self,valor):
        self._valor = valor
    @property
    def valor(self):
        return self._valor 
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
class Deposito(Transacao):
    def __init__(self,valor):
        self._valor = valor
    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)  




def sacar(clientes):
    cpf = input("informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf,clientes)
    if not cliente:
        print("cliente nao encontrado")
        return
    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta,transacao)

def criar_cliente(clientes):
     cpf = input("informe o CPF do cliente: ")
     cliente = filtrar_cliente(cpf,clientes)
     if  cliente:
        print("cliente ja existe")
        return 
     nome = input("Informe o nome do cliente: ")
     data_nascimento = input("informe a data de nascimento: ")  
     endereco = input("informe o endereco ")
     cliente = PessoaFisica(nome = nome,data_nasc=data_nascimento,cpf = cpf,endereco = endereco)
     clientes.append(cliente)
     print("Cliente cadastrado com sucesso")
     

def listar_contas(contas):
    for conta in contas:
        print("=" *100)
        print(textwrap.dedent(str(conta)))

def criar_conta(numero_conta,clientes,contas):
    cpf = input("informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf,clientes)
    if not cliente:
        print("cliente nao encontrado")
        return
    conta = ContaCorrente.nova_conta(cliente=cliente , numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n #### Conta criada com sucesso ###")

def exibir_extrato(clientes):
    cpf = input("informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf,clientes)
    if not cliente:
        print("cliente nao encontrado")
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("")
    print("########### EXTRATO ###########")
    transacoes = conta.historico.transacoes
    extrato = ""
    if not transacoes:
        extrato = "Nao foram realizadas movimentacoes"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR${transacao['valor']:.2f}"
        print(extrato)
        print(f"\nSaldo: \n\nR$ {conta.saldo:.2f}")
        print("###############################")

def filtrar_cliente(cpf,clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf ==cpf ]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente nao possui conta!!")
        return

    return cliente.contas[0]
def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf,clientes)
    if not cliente:
        print("Cliente nao encontrado!!")
        return
    valor = float(input("informe o valor do deposito: "))
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    cliente.realizar_transacao(conta,transacao)
def menu():
    clientes = []
    contas = []
    menu = """########### MENU #############
# 1 - Deposito	             #
# 2 - Saque                  #
# 3 - Extrato                #
# 4 - Criar Usuario          #
# 5 - Criar Conta Corrente   #
# 6 - Listar contas          #
############################## """
    print(menu)
    resposta_input = int(input("informe sua operacao: "))
    resposta = int(resposta_input) 

    while resposta  in [1,2,3,4,5,6]:
        if resposta == 1:
            depositar(clientes)
        elif resposta == 2:
            print("Voce escolheu Saque")
            sacar(clientes)
        elif resposta == 3:
            print("Voce escolheu Extrato")
            print("")
            exibir_extrato(clientes)
        elif resposta == 4:
            print("Voce escolheu Criar usuario")            
            numero_conta = len(contas) + 1 
            criar_conta(numero_conta,clientes,contas)
        elif resposta == 5:
            print("Voce escolheu Criar Conta Corrente")
            criar_cliente(clientes)
        elif resposta == 6:
            print("Voce escolheu Listar contas")    
            listar_contas(contas)
        print(menu)
        
        resposta_input = input("selecione outra operacao: ")
        resposta = int(resposta_input) 
    print("obrigado por usar nosso sistema!!")
    print("####################")


menu()
