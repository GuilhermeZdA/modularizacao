from .usuarios import Usuario
from .livros import Livro
from .emprestimos import Emprestimo

# Usar esse comando (uv run python -m mini_biblioteca.main)
# Path: ...\modularizacao\mini_biblioteca

def main():
    u1 = Usuario("Guilherme", "12345")
    l1 = Livro("PDD: guide book", "Guilherme Zacarias", "11111")

    print("Livro antes do emprestimo:")
    print(l1.disponivel)

    e1 = Emprestimo(l1, u1)

    print("Livro depois do emprestimo:")
    print(l1.disponivel)
    print("Estado do emprestimo:")
    print(e1.ativo)

    e1.devolver()

    print("Livro depois da devolução:")
    print(l1.disponivel)
    print("Emprestimo depois da devolução:")
    print(e1.ativo)

if __name__ == "__main__":
    main()