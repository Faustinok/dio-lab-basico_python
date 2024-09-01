#colecao que nao possiu objetos repetidos
set([1,2,3,1,3,4]) # 1,2,3,4
set("abacaxi") # b,a,x,i
set(("gol","palio","gol","ka"))
# set nao funciona em valores que nao sejam listas de itens

#metodos da classe Set
# conjuntos: 
#union
conjunto_a = {1,2,5}
conjunto_b = {1,2,3,4}
print(conjunto_a.union(conjunto_b)) 
#intersection (inner)
print(conjunto_a.intersection(conjunto_b)) 
#difference (left)
print(conjunto_b.difference(conjunto_a)) 
#difference (left)
print(conjunto_b.symmetric_difference(conjunto_a)) 

conjunto_a = {1,2,3,4,5}
conjunto_b = {1,2,3}

#issubset se o conjunto menor estiver inteiro no conjunto maior ele e um subset. 
print(conjunto_b.issubset(conjunto_a))
# Se o conjunto maior tiver todos os elementos do menor conjunto ele e um superset
print(conjunto_a.issuperset(conjunto_b))
#disjoint verifica se tem interseccao
conjunto_a = {1,2,3}
conjunto_b = {4,5,6}
print(conjunto_a.isdisjoint(conjunto_b))

#add  se o item nao existir ele sera adicionado ao conjunto
sorteio ={1,2}
sorteio.add(23)

sorteio.clear()
sorteio.copy()
sorteio ={1,2}
sorteio.discard(1)