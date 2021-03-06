import random

def Main():

    debug = input('Enter T to enter the randomly generated number: ')

    if debug == 'T':
        numbers = input(str('Enter the random numbers: '))
    else:
        while True:
            numbers = str(random.randint(0, 9999))
            if len(set(numbers)) == len(numbers):
                break

    count = 0
    while count < 10:

        if len(numbers) < 4:
            numbers = numbers.zfill(4)
        else:
            numbers = numbers

        while True:
            guess = input('Enter your guess: ')
            if len(guess) == 4:
                checker = guess.lstrip('0')
                if len(checker) == len(set(checker)):
                    break
                else:
                    print('Choose a guess that doesnt have consecutive numbers')
            else:
                print('Invalid Guess!!')


        bulls = 0
        cows = 0

        for i in range(len(numbers)):
            if guess[i] == numbers[i]:
                cows += 1
            elif guess[i] in numbers:
                bulls += 1

        print('\n{0} is incorrect\nCows: {1} \nBulls: {2}\n'.format(str(guess), str(cows), str(bulls)))

        if cows == 4:
            count = 10
            print('Congrats, you won the game!')

    print('Sorry, you lost the game the correct numbers were \n {0}'.format(str(numbers)))


if __name__ == '__main__':
    Main()