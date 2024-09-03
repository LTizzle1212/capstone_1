#  Part 1 & 2
class Author:  # creating a class called Author
    def __init__(self, name):
        self.name = name
        self.books = []  # empty list

    def publish(self, title):  # adding the publish method to the Author class
        if title in self.books:
            print('Sorry, this book name is a duplicate and already in use. Please use a new book name')
        else:
            self.books.append(title)

    def __str__(self):  #  adding the __str__ method that returns a string with the author's name and the name of their book titles
        if self.books:
            book_list = ', '.join(self.books)
        else:
            book_list = 'No books'
        return f'{self.name} Books Published: {book_list}'  # Concatenating the books published to make it look clean

King = Author('Stephen King')  # Adding a author
King.publish('The Shining')  # Adding a book
King.publish('The Running Man')  # Adding a book
King.publish('Different Seasons')  # Adding a book
print(King)


#  adding a main method to test the examples
def main():
    Logan = Author('Logan')
    Logan.publish('My Last Semester')
    Logan.publish('Always Hungry')
    Logan.publish('Always Hungry')  # this will print an error message due to duplicate books
    print(Logan)


main()  # have to call main methods




#  Part 3
from dataclasses import dataclass

@dataclass

class Student:  #  this is where the blocker starts for the Student class
        name: str #creating a string
        school_id: str #creating a string
        gpa: float #creating a float

        def __str__(self):
            return f'Name {self.name}, School ID: {self.school_id}, GPA: {self.gpa}' #Concatenating the name, schoolID & GPA


def main():  # This will create the instances
    Logan = Student('Logan', 'jd5497bg', 3.2)
    print(Logan)

    Issac = Student('Issac', 'po00989kj', 3.5)
    print(Issac)

    Samantha = Student('Samantha', 'fk04938dd', 3.8)
    print(Samantha)

main()  # have to call main methods after calling