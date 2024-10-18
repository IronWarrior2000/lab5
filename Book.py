class Book: 
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.read = False
        self.price = 0

    def setTitle(self, title): #Set the title of the book
        self.title = title
    
    def setAuthor(self, author): #set the author of the book
        self.author = author
    
    def setPages(self, pages): #Set the amount of pages in the book
        self.pages = pages

    def setPrice(self, price): #set the price of the book
        self.price = price
    
    def getTitle(self): #Get the title of the book
        return self.title
    
    def getAuthor(self): #Get the author of the book
        return self.author
    
    def getPages(self): #Get the amount of pages in the book
        return self.pages
    
    def getPrice(self): #Get the price of the book
        return self.price
    
    def markAsRead(self, read): #Set the read to True if read
        self.read = True

    def description(self): #Print out the description
        return f"Title:{self.title} \nAuthor:{self.author} \nPages:{self.pages} \nRead:{self.read}"