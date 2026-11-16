#упражнение 1
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


#упражнение 2
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


class Circle(Shape):
    PI = 3.14
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# упражнение 3
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise TypeError("Only instances of Book can be added")
        self.books.append(book)

    def find_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def count(self):
        return len(self.books)


#проверки
if __name__ == "__main__":
    print("--- BankAccount ---")
    acc = BankAccount("Анна", 100)
    print(f"Баланс: {acc.balance}")
    
    try:
        acc.balance = -5
    except ValueError as e:
        print(f"Ошибка присвоения: {e}")
        
    try:
        acc.withdraw(500)
    except ValueError as e:
        print(f"Ошибка снятия: {e}")
        
    acc.deposit(50)
    print(f"Баланс после пополнения: {acc.balance}")

    print("\n--- Shapes ---")
    circle = Circle(2)
    rect = Rectangle(3, 4)
    print(f"Is circle a Shape? {isinstance(circle, Shape)}")
    print(f"Is rectangle a Shape? {isinstance(rect, Shape)}")
    
    for s in (Circle(1), Rectangle(2, 5)):
        print(f"Площадь: {s.area()}")

    print("\n--- Library ---")
    l1 = Library()
    l2 = Library()
    b1 = Book("Преступление и наказание", "Достоевский")
    
    l1.add_book(b1)
    print(f"l1 count: {l1.count()}") # 1
    print(f"l2 count: {l2.count()}") # 0
    
    books_by_author = l1.find_by_author("Достоевский")
    print(f"Найдено книг Достоевского: {len(books_by_author)}")