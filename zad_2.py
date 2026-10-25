from zad_1 import Student

class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"Biblioteka w {self.city}, ul. {self.street}, (Otwarte: {self.open_hours} )"

class Employee:
    def __init__(self, first_name: str, last_name: str, hire_date: str, birth_date: str, city: str, street: str, zip_code: str, phone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"Pracownik: {self.first_name} {self.last_name}"

class Book:
    def __init__(self, library: Library, publication_date: str, author_name: str, author_surname: str, number_of_pages: int):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Książka '{self.author_name} {self.author_surname}' ({self.publication_date}) -> z {self.library}"

class Order:
    def __init__(self, employee: Employee, student: Student, books: list, order_date: str):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        books_str = "\n  - ".join([str(book) for book in self.books])
        return (f"--- Zamówienie z {self.order_date} ---\n"
                f"Obsługuje: {self.employee}\n"
                f"Dla: {self.student}\n"
                f"Wypożyczone książki:\n  - {books_str}\n")

if __name__ == "__main__":
    lib1 = Library("Warszawa","Lwowska","00-005","8:00-18:00","111-222-333")
    lib2 = Library("Kraków","Słoneczna","05-010","7:30-17:00","444-555-666")

    emp1 = Employee("Krzysztof","Kowalski","2010-03-15","1985-12-10","Łódź","Karmelicka","12-200","123-321-123")
    emp2 = Employee("Mariusz","Nowacki","2007-05-21","1978-10-14","Poznań","Zatorska","20-003","320-532-328")
    emp3 = Employee("Marysia","Jabłońska","2014-11-05","1990-08-22","Bydgoszcz","Cytrusowa","10-234","100-200-300")

    stud1 = Student("Adam Nowak", [30,70,90])
    stud2 = Student("Kamil Kowal", [80,90,75])
    stud3 = Student("Kamila Korzeniowska", [50, 45, 80])

    book1 = Book(lib1,"1995-10-15","Adam","Słowacki",345)
    book2 = Book(lib2,"1984-12-05","Juliusz","Prus",124)
    book3 = Book(lib1,"2012-04-23","Bolesław","Mickiewicz",345)
    book4 = Book(lib2,"2020-07-08","Andrzej","Szymborski",345)
    book5 = Book(lib1,"1993-01-27","Kazimierz","Małysz",345)

    order1 = Order(emp2,stud2,[book1, book4],"2026-03-08")
    order2 = Order(emp1,stud3,[book2, book3],"2026-05-26")

    print(order1)
    print(order2)