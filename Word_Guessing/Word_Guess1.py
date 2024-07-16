import time
import words
import random
def WordGuessing():
    """Word Guess 1"""
    try:
        Score=0
        print("Word Guessing 1\n")
        for Round in range(0,7):
            print("=============")
            print("Guess the Word")
            print(random.choice(words.EasyWordsblank))
            guess=str(input(">"))
            if(guess in words.EasyWordscomplete):
                print("\nCorrect✅")
                Score+=3
                continue
            else:
                print("\nWrong guess❌")
        print("================")
        print(f"You Scored {Score}%.")
        print("================")
        exit()
    except ValueError:
        print("\nNot allowed.")
        exit()


WordGuessing()