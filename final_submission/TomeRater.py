# TomeRater Capstone Project -- Gene Gathright


class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}  # {Book object: User's book rating}

    def get_email(self):
        """ Returns email associated with this user."""
        return self.email

    def change_email(self, new_email):
        """Takes in a new_email and changes the email for this user."""
        self.email = new_email
        print(f"Email for {self.name} has been updated!")
        return self.email

    def __repr__(self):
        return f"{self.name}, email: {self.email}, books read: {len(self.books)}"

    def __eq__(self, other):
        if self.name == other.name and self.email == other.email:
            return True
        return False

    def read_book(self, book, rating=None):
        """Adds {book: rating} to self.books{}."""
        self.books[book] = rating

    def get_average_rating(self):
        total_rating = 0.0
        number_ratings = 0

        for value in self.books.values():
            number_ratings += 1
            if value is not None:
                total_rating += value
        return total_rating / number_ratings


class Book(object):
    def __init__(self, title, isbn):
        self.title = title      # string
        self.isbn = isbn        # number
        self.ratings = []

    def get_title(self):
        """Returns the title of this book."""
        return self.title

    def get_isbn(self):
        """Returns the isbn of this book."""
        return self.isbn

    def set_isbn(self, new_isbn):
        """Takes in a new isbn and sets the book's isbn to this new number."""
        old_isbn = self.isbn
        self.isbn = new_isbn
        print(
            f"The isbn for the book '{self.title}' has been updated from '{old_isbn}' to '{self.isbn}'.")

    def add_rating(self, rating):
        """Takes in a rating and adds it to self.ratings []"""
        if rating >= 0 and rating <= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def __eq__(self, other):
        if self.title == other.title and self.isbn == other.isbn:
            return True
        return False

    def get_average_rating(self):
        return sum(self.ratings) / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return f"'{self.title}' | ISBN: {self.isbn}."


class Fiction(Book):
    def __init__(self, title, author, isbn):
        Book.__init__(self, title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return f"'{self.title}' by {self.author}"


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        Book.__init__(self, title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        article = "a" if self.level == "beginner" else "an"
        return f"'{self.title}', {article} {self.level} manual on {self.subject}"


# The application that stores the users:
class TomeRater:
    def __init__(self):
        self.users = {}  # {user's email: User object}
        self.books = {}  # {Book object: number of Users who've read it}

    def create_book(self, title, isbn):
        """Creates a new book with a title and isbn."""
        # new_book = Book(title, isbn)
        # return new_book
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        """Creates a new Fiction with title, author, isbn."""
        # new_fiction = Fiction(title, author, isbn)
        # return new_fiction
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        """Creates a new Non_Fiction with title, subject, level, isbn."""
        # new_non_fiction = Non_Fiction(title, subject, level, isbn)
        # return new_non_fiction
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        """ Adds book and rating to the user if user exists."""
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            if rating is not None:
                book.add_rating(rating)

            if book in self.books.keys():
                self.books[book] += 1
            else:
                self.books[book] = 1
        else:
            return f"No user with email {email}!"

    def add_user(self, name, email, user_books=None):
        # Create new User object from name and email.

        new_user = User(name, email)

        # Simple validation of email:
        for char in new_user.email.split():
            if char.find("@") == -1 or char.find(".") == -1:
                return "Invalid email syntax. Check email and try again."

            if new_user.email in self.users.keys():
                return f"Error! The email '{new_user.email}' already exists."
            else:
                # if email is okay, add user to self.users{}:
                self.users[email] = new_user
                # add books to users:
                if not isinstance(user_books, type(None)):
                    for book in user_books:
                        self.add_book_to_user(book, email)

    def print_catalog(self):
        """Iterates through self.books keys and prints them."""
        for book in self.books.keys():
            print(book)

    def print_users(self):
        """Iterates through self.users - {email: user obj} - and prints user obj."""
        for value in self.users.values():
            print(value)

    def most_read_book(self):
        """Iterates through all books in self.books - {book obj: num users who've read it} - and returns the most read book."""

        highest = 0
        most_read = ""

        for book, value in self.books.items():
            if value > highest:
                highest = value
                most_read = book.title
        return f"The most read book is '{most_read}' with {highest} readers."

    def highest_rated_book(self):
        """Iterates through all books in self.books -
        {book obj: num users who've read it} -
        and returns the book with highest avg rating."""
        highest_rated = 0.0
        top_rated_book = ""

        for book in self.books.keys():
            book_rating = book.get_average_rating()
            if book_rating > highest_rated:
                highest_rated = book_rating
                top_rated_book = book.title
        return f"'{top_rated_book}' is highest rated book with a rating of {highest_rated}."

    def most_positive_user(self):
        """Iterates through all users in self.users - {email: user obj - and returns user with highest average rating."""
        highest_user_rating = 0.0
        most_positive = ""

        for user in self.users.values():
            user_rating = user.get_average_rating()
            if user_rating > highest_user_rating:
                highest_user_rating = user_rating
                most_positive = user.name
        return f"The most positive user is {most_positive} with a rating of {highest_user_rating}."
