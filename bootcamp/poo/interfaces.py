from abc import ABC, abstractmethod

class Controle_remoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass
class Controle_tv(Controle_remoto):
    def ligar(self):
        print("ligando") 
    def desligar(self):
        print("desligando")

controle = Controle_tv()

controle.ligar()
controle.desligar()