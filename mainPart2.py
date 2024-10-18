from Book import * 
from Person import *
from mainPart1 import * 
#Import the classes from different files

def books(): #This function is to housed all of the books in the store
    
    #Setting the books
    mansfieldPark = Book("Mansfield Park", "Jane Austen", "488")
    grimmsFairyTales = Book("The Complete Grimm's Fairy Tales", "Jacob Grimm", "880")
    arabianNights = Book("The Arabian Nights", "Unknown", "1049")
    islandOfDrMoreau = Book("The Island of Dr. Moreau", "H.G. Wells","160")
    draculasQuest = Book("Dracula's Guest", "Bram Stoker", "20")
    authurAndHisKnights = Book("King Arthur and His Knights: Selected Tales", "Thomas Malory", "272")
    maryPoppinsComesback = Book("Mary Poppins Comes Back", "P.L. Travers", "312")    
    oedipusCycle = Book("The Oedipus Cycle: Oedipus Rex, Oedipus at Colonus, Antigone", "Sophocles", "259")
    oPioneers = Book("O Pioneers!", "Willa Cather", "159")    
    
    #Setting Prices for the books
    mansfieldPark.setPrice(29.99)
    grimmsFairyTales.setPrice(59.99)
    arabianNights.setPrice(59.99)
    islandOfDrMoreau.setPrice(24.99)
    draculasQuest.setPrice(24.99)
    authurAndHisKnights.setPrice(29.99)
    maryPoppinsComesback.setPrice(29.99)
    oedipusCycle.setPrice(19.99)
    oPioneers.setPrice(19.99)
    
    #Adding the books to a booklist and return the booklists
    booklists = [mansfieldPark, grimmsFairyTales, arabianNights, islandOfDrMoreau, draculasQuest, authurAndHisKnights, maryPoppinsComesback, oedipusCycle, oPioneers]
    return booklists


def userInput(prompt="Enter a number: "):#This will get the user to enter in a number to make everything run without extra lines
    try: #It will try to return the input with prompt
        return int(input(prompt))
    except ValueError: #Or it will enter in a value error and return -1
        print("Invalid input. Please enter a number.")
        return -1

def carting(booklists): #This is the shopping cart for the bookstore
    cart = [] #The cart lists
    while True: 
        #this will get the user input from the bookstore. User must select the corresponding numbers to the item (EX: 1. mansfieldpark)
        user = userInput("Select the number of the book to add to your cart (0 to stop): ")
        
        #if user select 0 it will break the while loop
        if user == 0:
            break
        #if the user is greater than 1 and less than the total amount of books in the booklists.
        #it will select the book item in the list and add it to the cart
        elif 1 <= user <= len(booklists):
            selected = booklists[user -1]
            cart.append(selected)
    return cart
    
def bookstore(): #This is the bookstore... a place to buy books
    total = 0 #Setting the total to 0
    print("What books would you like to buy?")
    print("Press 0 to end shopping list")
    
    #Getting the books for the book list
    booklists = books()
    
    #for the index and book when the booklist is enumerated it will print each book.
    for index, book in enumerate(booklists, 1):
        print(f"{index}. {book.description()}")
    
    #The cart will be sent back and add up all the prices of the books then print them out and returning the cart again
    cart = carting(booklists)
    total = sum(book.getPrice() for book in cart)
    print(f"Total Amount: ${total:.2f} \nTotal Items: {len(cart)}")
    return cart
    
def choices(person): #This is more so what do the person or user want to do as Choices. This is like what do you want to do such as Read a book, Buy a book, or check your collection of books.
    while True:
        print(f"What do you want to do? \n1. Read a book in your list? \n2. Buy a book from a bookstore \n3. View your book collection \n4. Exit")
        
        #This will get the menu to work
        user = userInput()
        
        #if the user selected 1 and if there are books in the list 
        if user == 1:
            if person.getBooklist():
                #It will print the collection and you can select what you want to read and it will mark it as read by the end
                print("Book Lists in Collection")
                for index, book in enumerate(person.getBooklist(), 1):
                    print(f"{index}. {book.description()}")
                    book_to_read = userInput("Enter the number of the book to read: ") - 1
                    person.readBook(book_to_read)
            else:
                #Else there is no books in the list
                print("You don't have any books to read.")
        
        #If user select 2
        elif user == 2:
            #The User will go to the "Bookstore" and for each item in the list it will add them to the person's book collection and print the total books in the list
            cart = bookstore()
            for item in cart:
                person.addBook(item)
            print(f"\nYou have purchased {len(cart)} books.")
        
        #If user select 3
        elif user == 3:
            #it will print out the person's collection
            print(person)
            
        #If user select 4
        elif user == 4:
            #It will end the loop which should end the program
            break
        else:
            #Else it will be an invalid option
            print("Invalid option. Please try again.")

def main():
    #Getting the person's name to make it more personal to the user
    personName = input("Enter in your name here!")
    person = Person(personName)
    try:
        #Give the person some choices to make
        choices(person)
        print("program ended")
            
    except ValueError: #Print out an ValueError if encountered
        print("ValueError")
    except IOError: #Print out an IOError if encountered
        print("ValueError")
    except FileNotFoundError: #Print out an FileNotFoundError if the Person and Book Class file is NOT found...
        print("ValueError")

main()