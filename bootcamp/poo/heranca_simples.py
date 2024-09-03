class Veiculo:
    def __init__(self,cor,placa,numero_rodas):

        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
    def ligar_motor(self):
        print("ligando motor")

class Motocicleta(Veiculo):
    pass
class Carro(Veiculo):
    pass
class Caminhao(Veiculo):
    pass

moto = Motocicleta("branco","123",2)
carro = Carro("vermelho","123",4)
caminhao = Caminhao("cinza","123",8)
moto.ligar_motor()
carro.ligar_motor()
caminhao.ligar_motor()