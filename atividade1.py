class Produto:
    def __init__(self, preco):
        self._preco = None
        self.preco = preco 

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor > 0:
            self._preco = valor
        else:
            raise ValueError("O preço deve ser maior que zero.")



