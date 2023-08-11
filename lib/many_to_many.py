class Author:
    count = 0
    def __init__(self, name):
        self.name = name
        Author.add_to_author_count()
    def add_to_author_count():
        Author.count += 1 

# The Author class should have the following methods:
#  []  contracts(self): This method should return a list of related contracts.
#  [] books(self): This method should return a list of related books using the Contract class  as an intermediary.
#  [] sign_contract(book, date, royalties): This method should create and return a new Contract object between the author and the specified book with the specified date and royalties
#  [] total_royalties(): This method should return the total amount of royalties that the author has earned from all of their contracts.


james_hawk = Author("James Hawk")
mason_hawk = Author("Mason Hawk")


class Book:
    count = 0 
    def __init__(self, title):
        self.title = title
        Book.add_to_book_count()
    def add_to_book_count():
        Book.count += 1


class Contract(Author, Book):
    count = 0
    def __init__(self, book, author, date, royalties):
        self.book = book
        self.author = author
        self.date = date
        self.royalties = royalties
        Contract.add_to_contract_count()
    def add_to_contract_count(self):
        Contract.count += 1

# contract_one = Contract("Harry")

# The author property should be an instance of the Author class, while the book property should be an instance of the Book class. The date property should be a string that represents the date when the contract was signed, while the royalties property should be a number that represents the percentage of royalties that the author will receive for the book.

# The Contract class should have the following methods:

# [] A class method contracts_by_date(cls, date): This method should return all contracts that have the same date as the date passed into the method.

        