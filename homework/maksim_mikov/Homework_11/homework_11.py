class Book:
    page_material = 'бумага'
    presence_of_text = True

    def __init__(self, book_title, author, number_of_page, isbn, reserved):
        self.book_title = book_title
        self.author = author
        self.number_of_page = number_of_page
        self.isbn = isbn
        self.reserved = reserved

    def reserve(self):
        if self.reserved:
            return "зарезервирована"

    def __str__(self):
        reserve_status = self.reserve() if self.reserved else ''
        return (f"Название: {self.book_title}, Автор: {self.author}, страниц: {self.number_of_page}, "
                f"материал: {self.page_material}, {reserve_status}, ").strip(' ,')


class PreSchoolBook(Book):
    availability_tasks = True

    def __init__(self, book_title, author, number_of_page, isbn, reserved, subject, graduate_class):
        super().__init__(book_title, author, number_of_page, isbn, reserved)
        self.subject = subject
        self.graduate_class = graduate_class

    def __str__(self):
        reserve_status = self.reserve() if self.reserved else ''
        return (f"Название: {self.book_title}, Автор: {self.author}, страниц: {self.number_of_page}, "
                f"предмет: {self.subject}, класс: {self.graduate_class}, {reserve_status}, ").strip(' ,')


first_book = Book("Ангелы и демоны", "Дэн Браун", 525, "978-5-93673-265-2", False)
second_book = Book("FRIENDS", "Saul Austerlitz", 368, "978-5-04-113253-8", False)
third_book = Book("Хочу и буду", "Михаил Лабковский", 320, "978-5-9614-6799-4", False)
four_book = Book("Friends, Lovers and the terrible thing", "Matthew Perry", 240, "978-5-04-188724-7", True)
fifth_book = Book("1984", "Джордж Оруэлл", 320, "978-5-17-148844-4", False)


first_preschool = PreSchoolBook("Алгебра", "Иванова А.И.", 186, "978-5-93675-265-2", False, "Математика", 9)
second_preschool = PreSchoolBook("Геометрия", "Геометричная Ю.В.", 230, "978-5-9556-265-2", False, "Геометрия", 10)
third_preschool = PreSchoolBook("Python это просто !", "Петров А.А.", 340, "978-5-93488-265-2", True, "Информатика", 8)


print(first_book)
print(second_book)
print(third_book)
print(four_book)
print(fifth_book)
print(first_preschool)
print(second_preschool)
print(third_preschool)
