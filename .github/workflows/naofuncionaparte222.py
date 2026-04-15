class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, percentual):
        desconto = self.preco * (percentual / 100)
        return self.preco - desconto

def teste():
    p = Produto("TV", 1000)
    resultado = p.aplicar_desconto(10)
    
    assert resultado == 900, f"Erro: esperado 900, veio {resultado}"

if __name__ == "__main__":
    teste()
    print("Teste passou")