"""
Cian Herlihy - R00205604 - Task 3

For Task 3 I needed to get an integer off the user and halve it if it is an Even number and times 3 + 1 if it is odd.
So to accomplish this I set up the converge() function to take in the int from the user and then determine if it is
Even, then I should divide by 2. I used modulus (%) for the mathematics to check if it is even. The only other option
then is odd so the else statement handles the multiplication by 3 and adding 1 to it. That is all the maths required 
for this function.

To make the program run in a loop until it reaches 1. Then I put it in a while loop. I simply put everything in a 
while loop for the exception handling to loop you back to input again and then another nested while loop to do the 
recursive function. I made the program sleep for 1/2 a second everytime it uses the function so it slows the program 
down to see the effect it has on the input number. This is not needed but more aesthetically pleasing in my opinion.

Exception handling includes handling of a ValueError which is a sting or float instead of an int for example. I have
an AssertionError to determine if the integer input is greater than 1. This is because the program would not need to
begin if the input was the number 1 since that is the end goal of the program. This makes the lowest possible
int to be 2 and it uses the function exactly once before exiting. 

I use sys.exit() to exit the program then when it has reached 1. However, it can be implemented to be an option to 
start the loop again if I wanted to allow multiple inputs at the users discretion. This would be simple by changing
the while loop to take a variable and only continue if they select the right option like in a menu.
"""
import sys
import time


def converge(recursive_int):
    if recursive_int % 2 == 0:
        recursive_int = recursive_int / 2
        print(int(recursive_int))
        return int(recursive_int)
    else:
        recursive_int = (recursive_int * 3) + 1
        print(int(recursive_int))
        return int(recursive_int)


def main():
    print("Task 3")
    print(f'{"=" * 30}')
    while True:
        try:
            print("")
            print("Even numbers are halved. Odd numbers are x3 and +1.")
            recursive_int = int(input("Enter an Integer >>> "))
            assert recursive_int > 1

            while True:
                time.sleep(0.5)
                recursive_int = converge(recursive_int)
                if recursive_int != 1:
                    continue
                else:
                    sys.exit()

        except AssertionError:
            print("Input number was too low.")
        except ValueError:
            print("Please Enter an Integer")


if __name__ == "__main__":
    main()
