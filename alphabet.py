import random, time, re
from wonderwords import RandomWord
from datetime import date

def rand():
    return random.randrange(1, 27)
def findHighscore():
    pattern = re.compile(rf'{numRounds} rounds —— \d+\.\d+ / (?P<avg>\d+\.\d+)')
    with open(rf'./logs/alphabet {gamemode}ing.txt', 'r') as logsFile:
        avgTimes = set()
        for line in logsFile:
            match = pattern.search(line)
            if match:
                avgTimes.add(float(match.group('avg')))
    return min(avgTimes, default=99999)
def intro():
    print('Welcome to Alphabet Mastery with Jake! For all your unnecessary alphabet needs!')
    print(f'Your current gamemode is "Super Fun & Fancy {gamemode.capitalize()}ing".')
    if highscore < 99999:
        print(f'Your current highscore for {numRounds} rounds is an average time of {highscore} seconds per round')
    print('When you are ready to start, type "start" and hit enter.')
    while True:
        if input() == 'start':
            break
        else:
            print('You must type the word "start" EXACTLY as shown. Try again.')
    print('Okay!')
    print('Ready, set, go!!!')
def outro(startGame, penalty = 0):
    endGame = time.time()
    totalTime = round(endGame - startGame + penalty, 3)
    averageTime = round((endGame - startGame + penalty) / numRounds, 3)
    
    star = ''
    if averageTime < highscore:
        star = '  *'
        print('* NEW HIGHSCORE! *')
    print(f'You completed {numRounds} rounds in {totalTime} seconds, for an average of {averageTime} seconds per round!')
    print('Thanks for playing!')
    print('  😁')
    logsFile = open(rf'./logs/alphabet {gamemode}ing.txt', 'a')
    logsFile.write(f'\n{date.today()}: {numRounds} rounds —— {totalTime:.3f} / {averageTime:.3f}{star}')
    logsFile.close()

def adding():
    counter = 0
    startGame = time.time()
    while counter < numRounds:
        x = chr(rand() + 64)
        y = chr(rand() + 64)
        print(x + ' + ' + y + ' =')
        while True:
            userInput = input()
            if userInput == 'q':
                exit()
            elif userInput == str(ord(x) + ord(y) - 128):
                print('Correct.')
                break
            else:
                print('Wrong! Try again')

    outro(startGame)
def reading():
    counter = 0
    startGame = time.time()
    while counter < numRounds:
        counter += 1
        word = RandomWord().word(word_min_length=7, word_max_length=11)
        numWord = []
        for i in word:
            numWord.append(ord(i) - 96)
        print(numWord)

        startWord = time.time()
        while True:
            userInput = input()
            if userInput == 'q':
                exit()
            elif userInput == word:
                endWord = time.time()
                print(f'Correct. That took {int(endWord - startWord + 0.5)} seconds.')
                break
            else:
                print('Wrong! Try again')

    outro(startGame)
def ordering():
    counter = 0
    penalty = 0
    startGame = time.time()
    while counter < numRounds:
        counter += 1
        x = chr(rand() + 64)
        y = chr(rand() + 64)
        print(x + ' ? ' + y)
        userInput = input()
        if userInput == 'q':
            exit()
        elif (userInput == '1' and x > y) or (userInput == '2' and x < y):
            print('Correct.')
        else:
            print('Wrong! +2 seconds')
            penalty += 2

    outro(startGame, penalty)

#prep
gamemode = 'read' #This can be set via input(), button, or here manually. Up to you.
if gamemode == 'read':
    numRounds = 6
elif gamemode == 'add':
    numRounds = 10
elif gamemode == 'order':
    numRounds = 25
highscore = findHighscore() #Keeping it at global scope
intro()

#actually running the game
if gamemode == 'read':
    reading()
elif gamemode == 'add':
    adding()
elif gamemode == 'order':
    ordering()

#outro() is inside each game function