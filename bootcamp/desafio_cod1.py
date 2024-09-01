def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_vendas = 0 
    for venda in vendas:
        total_vendas += venda
    media_vendas = total_vendas/len(vendas)
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()
    # TODO: Converta a entrada em uma lista de inteiros:
    lista_inteiros = entrada.split(",")
    vendas = list(map(int,lista_inteiros))
    return vendas

vendas = obter_entrada_vendas()
print(analise_vendas(vendas))