class Author:
    count = 0
    royalties = []
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
    def books(self):
        for contract in self.__contracts:
            if contract.book not in self.__books:
                self.__books.append(contract.book)
                return self.__books 
    def sign_contract(self, book, date, royalties):
        self.__contracts.append(Contract(self, book, date, royalties))
        # self.__books.append(book)
        # Append book object to list of books
        # return self.__contracts
        # To Do: 
    def total_royalties(self):
        total_royalties = sum(Author.royalties)
        return total_royalties
    
class Book:
    count = 0 
    def __init__(self, title):
        self.title = title
        # Below is a list of all contracts associated with an instance of the Book class. 
        self.__contracts_list = []
        self.add_to_book_count()
    def add_to_book_count(self):
        Book.count += 1
    def contracts(self):
        
            # Appends a string to the end of the self.__contract_list instead of a book object. 
            # Generator expression? 
        return self.__contracts_list
        # return [contract for contract in Contract.all if contract.book == self] 
    def sign_contract(self, contract):
    
        # new_contract = Contract(self, author, date, royalties)
        self.__contracts_list.append(contract)
        

        # Use a getter function to access the self.__contracts attribute in Author()? 
        # Assertion error is occurring because self.__contracts remains an empty list? 
    def authors(self):
        # authors = self.__contracts_list.filter(authors)
        return [contract.author for contract in self.__contracts_list]
        # Returns a list of the books authors.
        # Use a generator expression to create a list of authors 
    

    
        # return [author for author in Author.all if author.book == self ]
    # lIST Comprehension vs generator expression 
    
    












j_k_rowling = Author("J.K. Rowling")
harry_potter_sorcerer_stone = Book("Harry Potter and the Sorcer's Stone")

harry_potter_chamber_secrets = Book("Harry Potter and the Chamber of Secrets")

class Contract():
    count = 0
    def __init__(self, author, book, date, royalties):
        self.book = book
        if not isinstance(book, Book):
            raise Exception(" Please ensure book is a valid obj.")
        self.author = author
        if not isinstance(author, Author):
            raise Exception("Please enter a valid object")
        self.date = date
        if not isinstance(date, str):
            raise Exception("Please enter valid date")
        self.royalties = royalties
        if not isinstance(royalties, int):
            raise Exception("Please enter valid int.")
        # self.author.sign_contract(self)
        book.sign_contract(self)
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

        