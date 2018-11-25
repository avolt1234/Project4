import random

def Main():

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

        guess = input('Enter is your guess: ')
        #TODO create checker for repeated numbers in the input

        bulls = 0
        cows = 0

        for i in range(len(numbers)):
            if guess[i] == numbers[i]:
                cows += 1
            elif guess[i] in numbers:
                bulls += 1

        print('\nCows: {0} \nBulls: {1}'.format(str(cows), str(bulls)))

        if cows == 4:
            count = 10
            print('Congrats, you won the game!!!!')

    print(numbers)


if __name__ == '__main__':
    Main()