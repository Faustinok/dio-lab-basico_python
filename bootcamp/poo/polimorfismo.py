class Passaro:
    def voar(self): 
        print("voando...")

class Pardal(Passaro):
    def voar(self):
        return super().voar()
class Galinha(Passaro):
    def voar(self):
        print("galinha nao voa")

def plano_de_voo(obj):
    obj.voar()

p1 = Pardal()
p2 = Galinha()
plano_de_voo(p1)
plano_de_voo(p2)