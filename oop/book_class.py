class Book:
    def __init__(self, title, author, year):
        """initialising the book attribut"""

        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
       """ method to print a message when a book object is deleted"""
       print (f"Deleting '{self.title} by {self.author}, published in {self.year}")
    
    def __str__(self):
        """string representation of the book object"""
        return f"title:'{self.title}', by author:{self.author}, published in year:{self.year}."
    
    def __repr__(self):
        """Official representation of the Book object"""
        return f"Book('{self.title}', '{self.author}', {self.year})"
    
    
        

              
  

