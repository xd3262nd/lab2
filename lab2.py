from dataclasses import dataclass

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def publish(self, title):
        if title in self.books:
            print(f'{title} existed in the author profile. Please add a different book.')
        else:
            self.books.append(title)

    def __str__(self):
        books_list = ', '.join(self.books) or 'No books available'

        return f'Name: {self.name}. Books Published: {books_list} '

@dataclass
class Student:
    # With Dataclass, we do not need to initiate the init function and not having to repeat the attributes multiple times like the regular class
    name: str
    colleg_id: int
    gpa: float




def main():
    author1 = Author('user01')
    author1.publish('Hello World 1st edi')
    author1.publish('Hello World 2nd edi')
    author1.publish('Hello World 1st edi')


    print(author1)

    author2 = Author('user02')

    print(author2)

    student01 = Student('John D', 2342, 2.34)

    print(student01.name)


main()
