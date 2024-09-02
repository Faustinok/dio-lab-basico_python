class Bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo =modelo
        self.ano =ano
        self.valor = valor
    def correr(self):
        print("a bicicleta da cor {cor} esta correndo".format(cor = self.cor))
        print(self.__dict__)
    def buzinar(self):
         print("a bicicleta da cor {cor} buzina".format(cor = self.cor))
    def parar(self):
         print("a bicicleta da cor {cor} parou".format(cor = self.cor))


b1 = Bicicleta("vermelha","coral",2021,24.5)

b1.correr()


