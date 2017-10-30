
# coding: utf-8

# # BIOL5516 Assignment 03
# 
# #### Created :  *Berthin  Bitja*
# 
# 
# ### Note :
# For each of the following questions, please submit your code and a screenshot of the output. Note that for some questions, there are better (or worse) ways to accomplish a task, and that you should try to find the best solution! Please use comments to indicate which question you are addressing, and to describe what you are doing.

# ### Ex1
# 
# Write a program that uses a dictionary to store the author names for five different books. The program should ask the user for the name of a book, and should output the name of the author. Make sure that the user can exit the program, and let the user know if the book s/he has picked isn’t on file.
# 

# In[5]:

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


# ### Ex2
# 
# Write a program that plays a guessing game with a user. The program should pick a random number between 1 and 10, and then prompt the user to guess the number. It should keep going until the user guesses the correct number, and then output a message congratulating the user. It should also tell the user how many guesses s/he needed to get the right answer.

# In[5]:




# In[ ]:



