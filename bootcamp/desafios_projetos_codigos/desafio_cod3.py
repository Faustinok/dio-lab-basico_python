class Venda:
    def __init__(self, produto, quantidade, valor):
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor

class Relatorio:
    def __init__(self):
        self.vendas = []

    def adicionar_venda(self, venda):
        # TODOS: Verifique se o objeto passado é uma instância da classe Venda.
        if venda.__class__.__name__ =='':
            return False
        self.vendas.append(venda)
        

    def calcular_total_vendas(self):
        total = 0
        for venda in self.vendas:
            total += (venda.valor * venda.quantidade)
            
        return total


def main():
    relatorio = Relatorio()
    
    for i in range(3):
        produto = input()
        quantidade = int(input())
        valor = float(input())
        venda = Venda(produto, quantidade, valor)
        relatorio.adicionar_venda(venda)
    print(f"Total de Vendas: {relatorio.calcular_total_vendas()}")
    # TODOS: Exiba o total de vendas usando o método calcular_total_vendas.
    # Utilize o método `calcular_total_vendas` da classe `Relatorio` para mostrar o total acumulado das vendas.
    


if __name__ == "__main__":
    main()