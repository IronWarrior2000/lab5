from Book import *
#imported the book class to make this file functional

def main():
    #Set books
    theSun = Book("The Sun", "John Doe", "300")
    theMoon = Book("The Moon", "Jane Doe", "210")
    theSun.markAsRead(True)

    booklist = [theSun, theMoon]
    
    for items in booklist:
        print(items.description())
    return booklist

main()