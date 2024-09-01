# declarando uma lista
frutas =["morango","maca","uva","pera"]
print(len(frutas))
produtos =[]
letras = list("python")
numeros = list(range(10))
lista2 = ["abc",1,2,3,[1,3,4]]

print(frutas[0]) #morango
print(frutas[-2]) #uva
print(lista2[4][2]) #4
print(frutas[0:2]) #morango,maca
print(frutas[2:]) #"uva","pera"
for f in frutas:
    print(f)

frutas.append("banana")


#metodos da classe list

lista3 = [1,2,3,3]
lista4 = lista3.copy()
print(lista4.count(3))

lista4.extend(frutas)
for f in lista4:
    print(f)
lista4.pop()#remove o ultimo elemento
lista4.pop(3)#remove o elemento por indice
lista4.remove(3) #remove o ultimo elemento 3 na lista
lista4.sort() # ordena
lista4.sort(reverse= True) #reverte
lista4.sort(key=lambda x: len(x)) # vai ordenar de acordo com o tamanho do item 
len(lista4) #mostra o tamanho da lista


# TUPLAS  #

# uma lista imutavel 
frutas = ("laranja","maca","uva",)
letras = tuple("python")
numeros = tuple([1,2,3,4])
print(frutas[2])