

import random


""" def guess_random_number(tries, start, stop):
    
    number = random.randint(start, stop)

    while tries != 0:
        
        print("Number of tries lelf:", tries)

        print("Guess a number between", start, "and", stop)

        guess = int(input("Make a Guess:"))

        if guess == number:
            print("You guessed the correct number!")
            #return ()
      
        elif guess < number:
            print("Guess higher!")

            tries = tries - 1

      
        elif guess > number:
            print("Guess lower!")

            tries = tries - 1

        else:
            break
    print("You have failed to guess the number: ")  """

#Driver code Task1
#guess_random_number(5, 0, 10)


#Task 2 using linear search function

""" def guess_random_number_linear(tries, start, stop):

    number = random.randrange(start, stop)

    number = int(input("The number for the program to guess is: "))
    
    for number in range(start, stop):
        tries != 0
        print("Number of tries lelf:", tries)
        print("The program is guessing... ",number)
        tries = tries - 1
        if tries <= 0:
            print("You have failed to guess the number!")
            
            return number        
               
#Driver code Task2
guess_random_number_linear(5, 0, 5)  """


#Task 3 using binary search function

def guess_random_number_binary(tries, start, stop):

    number = random.randint(start, stop)

    user = int(input("Random number to find: "))
    
    tries != 0

    pivot_value = (user + number) // 2

    while user != number:
        tries -= 1 

        if user == number: 
           print("Found it! ", number)
        
        elif user > pivot_value:
            start = pivot_value + 1
            pivot_value = (start + stop) // 2
            print("Guessing higher!")

        elif user < pivot_value:
            stop = pivot_value - 1
            pivot_value = (start + stop) // 2
            print("Guessing lower!")

        else:
            print("Your program failed to find the number")
            break


               
#Driver code Task3

guess_random_number_binary(5, 0, 100) 



    

