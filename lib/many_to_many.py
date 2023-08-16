class Author:
    count = 0
    royalties = []
    books = []
    def __init__(self, name):
        self.name = name
        self.__contracts = []
        self.__books = []
        self.add_to_author_count()
    def add_to_author_count(self):
        Author.count += 1 
    def add_to_royalties(self):
         self.author.royalties.append(self)
    def contracts(self):
        return self.__contracts
    def sign_contract(self, book, date, royalties):
        self.date = date
        self.royalties = royalties
        new_contract = Contract(self, book, date, royalties)
        self.__contracts.append(new_contract)
        # self.__books.append(book)
        # Append book object to list of books
        return self.__contracts 
    def total_royalties(self):
        total_royalties = sum(Author.royalties)
        return total_royalties
    def books(self):
        for contract in self.__contracts:
            if contract.book not in self.__books:
                self.__books.append(contract.book)
                return self.__books 


        new_book = Book(self)
        self.__books.append(new_book)
        return self.__books
        
    

# The Author class should have the following methods:
#  [] contracts(self): This method should return a list of related contracts.
#  [] books(self): This method should return a list of related books using the Contract class as an intermediary.
#  [] sign_contract(book, date, royalties): This method should create and return a new Contract object between the author and the specified book with the specified date and royalties
#  [] total_royalties(): This method should return the total amount of royalties that the author has earned from all of their contracts.

class Book:
    count = 0 
    contracts = [] 
    def __init__(self, title):
        self.title = title
        self.add_to_book_count()
    def add_to_book_count(self):
        Book.count += 1

j_k_rowling = Author("J.K. Rowling")
harry_potter_sorcerer_stone = Book("Harry Potter and th Sorcer's Stone")
harry_potter_chamber_secrets = Book("Harry Potter and the Chamber of Secrets")

class Contract():
    count = 0
    def __init__(self, author, book, date, royalties):
        self.book = book
        if not isinstance(book, Book):
            raise Exception(" Please ensure book is a valid obj.")
        self.author = author
        self.date = date
        if not isinstance(date, str):
            raise Exception("Please enter valid date")
        self.royalties = royalties
        if not isinstance(royalties, int):
            raise Exception("Please enetr valid int.")
        self.author.contracts().append(self)
        self.add_to_contract_count()
    def add_to_contract_count(self):
        Contract.count += 1
    @classmethod
    def contracts_by_dates(cls, date):
        pass
    # raise
# Must throw an exception if the user passes in a string instead of an object. 
# Try/except statement 

contract_one = Contract(j_k_rowling, harry_potter_sorcerer_stone, '01/01/2001', 40000)
contract_two = Contract(j_k_rowling, harry_potter_chamber_secrets, '01/01/2001', 40000)


# The author property should be an instance of the Author class, while the book property should be an instance of the Book class. The date property should be a string that represents the date when the contract was signed, while the royalties property should be a number that represents the percentage of royalties that the author will receive for the book.

# The Contract class should have the following methods:

# [] A class method contracts_by_date(cls, date): This method should return all contracts that have the same date as the date passed into the method.

        