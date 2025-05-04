import random

word_bank = ['nostalgia', 'prejudice', 'solitude', 'yawn', 'sigh']

word=random.choice(word_bank)

guessedWord= ['_'] * len(word)

attempts=10

while attempts>0:
    print('\nCurrent Word: '+''.join(guessedWord))
    guess=input('\nGuess a letter')
    
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guessedWord[i]=guess
        print('\nGreat guess!')

    else:
        attempts-=1
        print('\nSorry your guess is wrong! You have '+ str(attempts)+ ' attempts left.')

    if '_' not in guessedWord:
        print('\n Congratulations! You have guessed the word '+word)
        break

if '_' in guessedWord:
    print(f'\nYou have run out of attempts. The word was: {word}')  

     

