from .livros import Livro
from .usuarios import Usuario

class Emprestimo:
    def __init__(self, livro: Livro, usuario: Usuario):
        if not livro.disponivel:
            raise ValueError("ERRO! Não é possivel emprestar um livro que não está disponivel")
        
        self.livro = livro
        self.usuario = usuario
        self.ativo = True

        self.livro.disponivel = False


    def devolver(self) -> None:
        self.ativo = False
        self.livro.disponivel = True