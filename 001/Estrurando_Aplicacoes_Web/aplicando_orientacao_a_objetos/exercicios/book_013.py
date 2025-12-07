# 1- Crie uma classe chamada Livro com um construtor que aceita os parâmetros titulo, autor e ano_publicacao.
class Book:

    # 8.1- add class attribute books_list
    books_list = []

    def __init__(self, title: str, author: str, year_of_publication: int):
        self._title = title
        self._author = author
        self._year_of_publication = year_of_publication

        # 2- Inicie um atributo chamado disponivel como True por padrão.
        self._available = True

        # 8.2- add book(self), every time a Book() is created, to book_list
        # Append the instance to the class's tracking list.
        Book.books_list.append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year_of_publication(self):
        return self._year_of_publication

    @property
    def available(self):
        return self._available

    # 3- Na classe Livro, adicione um método especial str que retorna uma mensagem formatada com o título, autor e ano de publicação do livro.
    def __str__(self):
        return f"""
        {'Title:':<15} {self._title:<15}
        {'Author:':<15} {self._author:<15}
        {'Publication:':<15} {self._year_of_publication}"""

    # 6- Adicione um método de instância chamado emprestar à classe Livro que define o atributo disponivel como False.
    def borrow(self):
        self._available = False

    # 7.1- Is not in the exercise, but it is better to show the result
    def formatted_available(self):
        if self._available:
            return "available"
        return "borrowed"

    # 8- Adicione um método estático chamado verificar_disponibilidade à classe Livro que recebe um ano como parâmetro e retorna uma lista dos livros disponíveis publicados nesse ano.
    @classmethod
    def check_availability(cls, year: int):
        book_available = []

        for publication in Book.books_list:
            if publication._year_of_publication == year:
                if publication._available:
                    book_available.append(publication)

        return book_available

    @classmethod
    def print_availability(cls, year: int):
        print(f"Checking for available books from {year}")
        is_available = cls.check_availability(year)
        if not is_available:
            print(f"There are no books available published in the year {year}.")
        else:
            for book in is_available:
                print(book)


# 4- Crie duas instâncias da classe Livro e
book1 = Book("Dom Casmurro", "Machado de Assis", 1899)
book2 = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 1997)

# 5- imprima essas instâncias.
print(book1)
print(book2)

# 7- Crie uma instância da classe, chame o método emprestar e imprima se o livro está disponível ou não.
book3 = Book("Twilight", "Stephenie Meyer", 2005)
book3.borrow()
print(f"\nIs book '{book3.title}' available? {book3.available}")

# 7.1- after create formated_available
print(f"\nThe book '{book3.title}' is {book3.formatted_available()}.")

# 8.3- Implementing @classmethod check_availability
book4 = Book("Memoirs of a Geisha", "Arthur Golden", 1997)
print()
Book.print_availability(1997)
print()
Book.print_availability(2000)
print()
Book.print_availability(2005)
