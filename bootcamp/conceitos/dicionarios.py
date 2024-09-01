pessoa = {"nome": "Gabs", "idade": 28 ,"dados":{"email": "faustinoknada@gmaill.com","teste": 1}} 
pessoa2 = dict(nome="faustinok",idade =29)
pessoa["telefone"] = "123232"
print(pessoa["nome"])
pessoa["telefone"]  =2
print(pessoa)

for chave in pessoa:
    print(chave,pessoa[chave])

#funcoes
#clear -> apaga todos os valores do dict 
pessoa2.clear()
print(pessoa2)
#copy ->copia ???

#fromkeys -> cria chaves 1 - cria chaves mas sem nenhum valor 2 - cria chaves com valor padrao 
dict.fromkeys(["nome","telefone"])
dict.fromkeys(["nome","telefone"],"vazio")

#get forma de acessar valores no dict

pessoa = {"nome": "Gabs", "idade": 28 ,"dados":{"email": "faustinoknada@gmaill.com","teste": 1}} 
# pessoa["teste"] -> da erro porque a chave nao existe
pessoa.get("teste") #none
pessoa.get("chave",{}) # {}
pessoa.get("nome",{}) #"Gabs"

# items retorna uma lista de tuplas 
print("####################")
print(pessoa.items())

#keys retorna so as chaves 
print(pessoa.keys())

# pop remove uma chave 
pessoa.pop("dados")
print(pessoa)
pessoa.pop("dados",{}) #se nao encontrar a chave, retorna oq eu quero

#popitem remove o item ?? nao entendi

#setdefault se o item nao estiver no dicionario ele coloca um default 
# se o atributo existe, ele retorna o valor e nao altera ele
pessoa.setdefault("chave", "valor") #valor
pessoa.setdefault("nome", "gafds") #gabs

#update 
pessoa.update({"nome": "Gabs", "idade": 28 })
print(pessoa)

# values retorna todas as chaves 
print(pessoa.values())

#in verifica se uma chave existe ou nao no dict (true or false)
print("nome" in pessoa)