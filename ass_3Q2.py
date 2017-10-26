# 2. Write a program that plays a guessing game with a user. The program should
# pick a random number between 1 and 10, and then prompt the user to guess
# the number. It should keep going until the user guesses the correct number,
# and then output a message congratulating the user. It should also tell the
# user how many guesses she needed to get the right answer.

from random import randint

guess = False
number_of_guess = 10
number = randint(1, 10)

# initialize the data
usr_msg_1 = "Pick a number between 1 and 10: "
usr_msg_2 = "Pick another number between 1 and 10: "

user_number = input(usr_msg_1)
while not guess:
    number_of_guess -= 1
    if user_number == number:
        print 'You guessed the right number: {}'.format(user_number)
        print 'You have {} guesses remaining'.format(number_of_guess)
        print 'Thanks for playing !!!!'
        break
    if user_number != number and number_of_guess > 0:
        print 'You have {} guesses remaining'.format(number_of_guess)
        user_number = int(input(usr_msg_2))
    if number_of_guess == 0 :
        print 'sorry no more guess, you lost'
        break
    if user_number == 'exit' :
        break




