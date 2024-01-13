#Classes and Objects

class Book:
    def __init__(self, title, author, genre):
        
        self.title = title
        self.author = author
        self.genre = genre

    def set_information(self, title, author, genre):
    
        self.title = title
        self.author = author
        self.genre = genre

    def display_information(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")

book_instance = Book(title="The Catcher in the Rye", author="J.D. Salinger", genre="Fiction")

book_instance.display_information()

book_instance.set_information(title="To Kill a Mockingbird", author="Harper Lee", genre="Classic")
print("\nAfter Updating Information:")
book_instance.display_information()
