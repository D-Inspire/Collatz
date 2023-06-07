

# print('enter your name')
# number = int(input())
# while number != 1:
#     if number % 2 == 0:
#         number = number // 2
#         print(number)
#     elif number % 2 == 1:
#         number = 3 * number + 1
#         print(number)


# define a funtion collatz() with a single parameter 'number'
def collatz(number):
    while number != 1:
        # If collatz is even, print and return the value number // 2
        if number % 2 == 0:
            number = number // 2
            print(number)
        # If collatz is odd, print and return 3 * number + 1
        elif number % 2 == 1:
            number = 3 * number + 1
            print(number)

        try:
            number = int(number)
            print("thank you")

        except ValueError:
            print("it must be an integer")
    print('work done with zero error')

def my_work():
    print('enter your name')
    number = int(input())
    collatz(number)
my_work()