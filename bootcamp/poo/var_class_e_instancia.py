class Pessoa: 
    def __init__(self,nome,idade):
        self.nome = nome 
        self.idade = idade
    @classmethod 
    def criar_de_data(cls,ano,nome):
        idade = 2024 - ano
        return cls(nome,idade)
        
p = Pessoa("gab",28)
print(p.nome,p.idade)
p2 = Pessoa.criar_de_data(1996,"gabriel")
print(p2.nome)