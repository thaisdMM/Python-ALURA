# 9- Crie um arquivo chamado biblioteca.py e importe a classe Livro neste arquivo.
from book_013 import Book


# 10- No arquivo biblioteca.py, empreste o livro chamando o método emprestar e

book5 = Book("Fifty Shades of Grey", "E. L. James", 2011)


print(f"\nIs the book '{book5.title}' borrowed or available?")
print(f"{book5.title} is {book5.formatted_available()}\n")

# 12- No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
Book.print_availability(2011)

# 10- No arquivo biblioteca.py, empreste o livro chamando o método emprestar e
print(f"\nBorrowing the Book: {book5.title}")
book5.borrow()

# 11- imprima se o livro está disponível ou não após o empréstimo.
print(f"\nIs the book '{book5.title}' borrowed or available?")
print(f"{book5.title} is {book5.formatted_available()}.\n")

# 12- No arquivo biblioteca.py, utilize o método estático verificar_disponibilidade para obter a lista de livros disponíveis publicados em um ano específico.
Book.print_availability(2011)
