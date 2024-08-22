from produto import Produto 

produto = Produto("Computador", 2100.0, 900.0)
print(f"Descrição: {produto.get_descricao()}")
print(f"Preço: {produto.get_preco()}")
print(f"Custo: {produto.get_custo()}")

margem = produto.calcula_margem()
print(f"Margem de lucro: {margem:.2f}%")
