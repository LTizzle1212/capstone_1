class Author:  # creating a class called Author
    def __init__(self, name):
        self.name = name
        self.books = []  # empty list

    def publish(self, title):  # adding the publish method to the Author class
        self.books.append(title)

    def __str__(self):  # adding the __str__ method that returns a string with the author's name and the name of their book titles
        if self.books:
            book_list = ', '.join(self.books)
        else:
            book_list = 'No books'
        return f'{self.name} Books Published: {book_list}'  # Concating the books published to make it look clean

King = Author('Stephen King')
King.publish('The Shining')
King.publish('The Running Man')
King.publish('Different Seasons')
print(King)


#adding a main method to test the examples
def main():
    Logan = Author('Logan')
    Logan.publish('My Last Semester')
    Logan.publish('Always Hungry')
    print(Logan)


main()  # have to call main methods after defining a main method