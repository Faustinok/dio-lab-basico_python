#maiuscula minuscula e titulo 
test_string = "gabriel"
print(test_string.upper())
print(test_string.lower())
print(test_string.title())

#eliminar espacos 
test_string = "    gabriel     "
print(test_string.strip())
print(test_string.lstrip())
print(test_string.rstrip())
# juncoes e centralizacoes 
curso = "abc"
print(curso.center(10,"#"))
print(".".join(curso))