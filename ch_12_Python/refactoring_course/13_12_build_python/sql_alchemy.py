from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Создание базы данных SQLite в памяти
engine = create_engine('sqlite:///books_authors.db', echo=True)
Base = declarative_base()

# Ассоциативная таблица для отношения "многие ко многим" между книгами и авторами
books_authors = Table('books_authors', Base.metadata,
                      Column('author_id', Integer, ForeignKey('authors.id')),
                      Column('book_id', Integer, ForeignKey('books.id')))

# Модель для авторов
class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship('Book', secondary=books_authors, back_populates='authors')

    def __repr__(self):
        return f"<Author(name={self.name})>"

# Модель для книг
class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    authors = relationship('Author', secondary=books_authors, back_populates='books')

    def __repr__(self):
        return f"<Book(title={self.title})>"

# Создание всех таблиц в базе данных
Base.metadata.create_all(engine)

# Создание сессии для взаимодействия с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Добавление данных (авторов и книг)
author1 = Author(name='J.K. Rowling')
author2 = Author(name='George R.R. Martin')
book1 = Book(title='Harry Potter and the Philosopher\'s Stone')
book2 = Book(title='Harry Potter and the Chamber of Secrets')
book3 = Book(title='A Game of Thrones')
book4 = Book(title='A Clash of Kings')

# Связь книг с авторами
author1.books = [book1, book2]
author2.books = [book3, book4]

# Добавление объектов в сессию
session.add_all([author1, author2])
session.commit()

# Вывод информации о книгах, написанных авторами
authors = session.query(Author).all()
for author in authors:
    print(f"{author.name} wrote the following books:")
    for book in author.books:
        print(f"- {book.title}")

# Закрытие сессии
session.close()