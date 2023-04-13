import os
from time import sleep
from typing import List


class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year
        self.shelf = None

    def book_added(self, shelf_name: str):
        self.shelf = shelf_name


class Shelf:
    def __init__(self, name: str, capacity: int = 6):
        self.name = name
        self.capacity = capacity
        self.used_space = 0
        self.width = 2
        self.height = 3
        self.paint_head = "██" * (self.width + 1 + (self.width * 2))
        self.paint_body = "██" + "    ██" * 3
        self.books = dict()

    def add_book(self, book: Book):
        if self.used_space < self.capacity:
            self.used_space += 1
            self.books.setdefault(len(self.books), book)
            book.book_added(self.name)
            return "Book was added"
        else:
            return "There is no space. Buy some space at this number\n+7(967)593-24-27"

    def get_painted_shelf_body(self):
        do_string = [*[" ❖❖ "] * self.used_space, *["    "] * (self.capacity - self.used_space)]
        result = []
        for i in range(self.height):
            result.append([])
            for j in range(self.width):
                result[i].append(do_string[j + i * 2])
        return result

    def get_name(self):
        spaces = 17 - len(self.name)
        return self.name + " " * spaces


class Room:
    def __init__(self):
        self.shelves = dict()
        self.shelves_name = dict()
        self.genres = set()

    def add_new_shelf(self, new_shelf: Shelf):
        self.shelves.setdefault(new_shelf.name, new_shelf)
        self.genres.add(new_shelf.name)


def make_a_stroke(lst: List):  # [[[o],[o]], [[o],[o]], [o],[o]]]
    stroke = []
    for i in lst:
        stroke.append(f"{THREE_SPACES}██")
        for j in i:
            stroke.append(f"{j}██")
    return "".join(stroke)


def answer_observer(fun_answer: int):
    if fun_answer == 1:
        title = input("title: ")
        author = input("author: ")
        genre = input(f"genre {room.genres}: ")
        if genre not in room.genres:
            return "You have not shelf for this genre"
        try:
            year = int(input("year of writing of the book: "))
            book = Book(title, author, genre, year)
            books_shelf = room.shelves[genre]
            return books_shelf.add_book(book)

        except ValueError:
            print("incorrect value (\"ValueError\")")
    elif fun_answer == 2:
        title = input("title: ")
        indexes = []
        for shelf_index, values in room.shelves.items():
            for books_index, cur_book in values.books.items():
                if cur_book.name == title:
                    indexes.append([shelf_index, books_index // 2 + 1, (books_index & 1) + 1])
        return indexes


os.system("cls")
THREE_SPACES = "   "
room = Room()
room.add_new_shelf(Shelf("Fantasy"))
room.add_new_shelf(Shelf("History"))
room.add_new_shelf(Shelf("Drama"))
answer = 0
head_len = 14
while True:
    paint_head = [THREE_SPACES]
    paint_body = []
    paint_whole_body = []
    up_head = [THREE_SPACES]
    for shelf in room.shelves.values():
        paint_head.append(shelf.paint_head)
        up_head.append(shelf.get_name())
        paint_head.append(THREE_SPACES)
        paint_body.append(shelf.get_painted_shelf_body())
    for i in range(len(paint_body[0])):
        jerk = []
        for j in range(len(paint_body)):
            jerk.append(paint_body[j][i])
        paint_whole_body.append(make_a_stroke(jerk))
    print(*up_head, sep="")
    print(*paint_head, sep="")
    for i in paint_whole_body:
        for j in range(3):
            print(i)
        print(*paint_head, sep="")
    if not answer:
        print("\nAdd book - 1")
        print("Select book - 2")
        print("Shop - 3")

        try:
            answer = int(input())
        except ValueError:
            print("incorrect value (\"ValueError\")")
            sleep(1.4)
    else:
        print()
        if answer == 2:
            this_cod = answer_observer(answer)
            if this_cod:
                for i in this_cod:
                    print(room.shelves[i[0]].name, *i[1:])
                input()
            else:
                print("There is no book with this title")
                sleep(1.4)
        else:
            print(answer_observer(answer))
            sleep(1.4)
        answer = 0
    os.system("cls")

    # TODO сохранение данных
    # TODO раскраска  в цвета
    # TODO донат на добавление новых полок (длина названия должна быть меньше head)
    # TODO донат на увеличение объема (тоесть высоты)
    # TODO потом на добавление самой полочки (новой)
