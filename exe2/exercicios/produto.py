class Produto:
  def __init__(self, descricao, preco, custo):
    self.descricao = descricao
    self.preco = preco
    self.custo = custo

  def get_descricao(self):
    return self.descricao
  def set_descricao(self, descricao):
    self.descricao = descricao
  def get_preco(self):
    return self.preco
  def set_preco(self, preco):
    self.preco = preco
  def get_custo(self):
    return self.custo
  def set_custo(self, custo):
    self.custo = custo

  def calcula_margem(self):
    return (self.custo/self.preco)*100
  