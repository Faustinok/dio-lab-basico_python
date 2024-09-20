class Carro:
    def __init__(self,nome):
        self._nome = nome
        self._motor = None
        self._fabricante = None
    @property 
    def nome(self):
        return self._nome
    @property 
    def motor(self):
        return self._motor
    @property 
    def fabricante(self):
        return self._fabricante               
    @motor.setter
    def motor(self,valor):
        self._motor = valor
        
    @fabricante.setter
    def fabricante(self,valor):
        self._fabricante = valor    
class Motor:
    def __init__(self,nome):
        self._nome = nome 
    @property
    def nome(self) :
        return self._nome
class Fabricante:
    def __init__(self,nome):
        self._nome = nome
    @property
    def nome(self):
        return self._nome

focus = Carro('Focus Titanium')
ford = Fabricante('Ford')
motor_2_0 = Motor('2.0')
focus.fabricante = ford
focus.motor = motor_2_0
print (focus.nome,focus.fabricante.nome,focus.motor.nome)