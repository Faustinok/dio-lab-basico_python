class Animal:
    def __init__(self,nro_patas):
        self.nro_patas = nro_patas
class Mamifero(Animal):
    def __init__(self, cor_pelo,**kw):
        self.cor_pelo =cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self,cor_pena,**kw ):
        self.cor_pena =cor_pena
        super().__init__(**kw)    
class Cachorro(Mamifero):
    def __str__(self):
         for chave,valor in self.__dict__.items():
            print (f"{chave}:{valor}")

class Ornintorrinco(Mamifero,Ave):
    def ue(self):
        print (self.__dict__.items())

#cachorro =Cachorro(4,"marrom")
orn =Ornintorrinco(cor_pena="preto",nro_patas=4,cor_pelo="marrom")
print(orn.ue())