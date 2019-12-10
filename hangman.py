import random

f= open('hangman_vocab_words.txt','r')
read_files= f.readlines()
word= random.choice(read_files)
f.close()


tries = 0
length_input = 0

while tries <=5:
    user_guess = input('Guess the Letter')
    if user_guess in word :
        for x in range(len(word)):
            if user_guess == word[x]:
                word=word.replace(user_guess,' ')
                print(word)
    else:
        tries = tries +1
        print(tries)

    if bool(word.strip()) == False:
        print('You \'ve WON!')
        break

print('Game Over')




