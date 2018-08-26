class User():
    def __init__(self, name, email):
        self.name = name
        self.email = email
        # Book object : rating
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("{} email has been updated to {}".format(self.name, self.address))

    def __repr__(self):
        return "User {}, email: {}, books read {}".format(self.name, self.email, len(self.books))

    def __eq__(self, other_user):
        pass

    def read_book(self, book, rating=None):
        # Add book object with rating to books dictionary
        self.books[book] = rating

    def get_average_rating(self):
        count = 0
        book_rating = 0
        for val in self.books.values():
            if val:
                count += val
                book_rating += 1
        avg = count / book_rating
        return int(avg)


class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        # List of ratings (numbers)
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("{}'s ISBN: {} has been updated" .format(self.title, self.isbn))

    def add_rating(self, rating):
        if (type(rating) == int) and (rating >= 0 or rating <= 4):
            self.ratings.append(rating)
        else:
            print("Invalid Rating!")

    def get_average_rating(self):
        count = 0
        user_rating = 0
        for rating in self.ratings:
            if rating:
                count += rating
                user_rating += 1
        avg = count / user_rating
        return int(avg)

    def __hash__(self):
        return hash((self.title, self.isbn))


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{} by {}" .format(self.title, self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.get_subject

    def get_level(self):
        return self.level

    def __repr__(self):
        # Test named arguments between {}
        return "{title}, a {level} manual on {subject}" .format(title=self.title, level=self.level, subject=self.subject)

class TomeRater():
    def __init__(self):
        # Contains users email : user object
        self.users = {}
        # Contains a book object : number of users who read it
        self.books = {}

    def create_book(self, title, isbn):
        book_object = Book(title, isbn)
        return book_object

    def create_novel(self, title, author, isbn):
        fiction_object = Fiction(title, author, isbn)
        return fiction_object

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction_object = Non_Fiction(title, subject, level, isbn)
        return non_fiction_object

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            # Get user object from self.users with email as key and call User.read_book
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with email {}" .format(email))

    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        # Add entry to users dictionary email : user object (name and email address)
        self.users[email] = user
        if user_books:
            for book in user_books:
                # Add book object (Title and ISBN) and email address
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book.title)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        most_read_num = max(self.books.values())
        for book in self.books:
            if self.books[book] == most_read_num:
                most_read = book
        return("'{}'." .format(most_read, most_read_num))

    def highest_rated_book(self):
        count = 0
        for book in self.books:
            avg_rating = book.get_average_rating()
            if avg_rating > count:
                count = avg_rating
                title = book
        return("'{}'".format(title))

    def most_positive_user(self):
        count = 0
        for user in self.users.values():
            avg_rating = user.get_average_rating()
            if avg_rating > count:
                count = avg_rating
                user = user
        return("'{}'" .format(user.name))




