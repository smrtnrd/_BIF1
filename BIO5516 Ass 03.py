library = {'BOOK A' :"Author A",
           'BOOK D': "Author D",
           'BOOK B':"Author B",
           'BOOK C' : "Author C",
           'BOOK E':"Author E"}

user_input = str(raw_input("Hello, what's the name of the book you are looking for: "))
message = "Not found"
book_name = user_input.upper()
is_found = False

while not is_found :
    if library.has_key(book_name) :
        print("this book was writter by " + library[book_name])
        is_found = True
    else :
        print (message)
        break





