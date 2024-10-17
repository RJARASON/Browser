import words
import random
import sys
def WordGuess():
    """Word Guess 2"""
    try:
        def Mainc():
            print("==============")
            print("Word Guessing 2")
            print("\nSelect game difficulty level") 
            print("1: Easy") 
            print("2: Medium") 
            print("3: Hard") 
            print("4: Extreme") 
            select=str(input(">")).lower()
            if(select==("1")):
                Easy()
            elif(select==("2")):
                Medium()
            elif(select==("3")):
                Hard()
            elif(select==("4")):
                Extreme()
            else:
                print("\nDifficulty unselected.")
        def Easy():
            E_Score=0
            print("\nDifficulty : EASY")
            for ou in range(5):
                print("Guess the Word")
                print(random.choice(words.EasyWordsblank))
                guess=str(input(">"))
                if(guess in words.EasyWordscomplete):
                    print("\nCorrect ✅.")
                    E_Score+=5/2
                    continue
                else:
                    print("\nWrong guess❌")
                    continue
            print("==================")
            print(f"\nYou Scored {E_Score}%.")
            print("PlayAgain? (Y/N)")
            prompt=str(input(">")).lower()
            if(prompt==("y")):
                WordGuess()
            elif(prompt==("n")):
                print("\nThanks For Playing.👋")
                sys.exit()
            print("==================")
            sys.exit()

        def Medium():
            M_Score=0
            print("\nDifficulty : MEDIUM")
            for ou in range(5):
                print("Guess the Word")
                print(random.choice(words.MediumWordsblank))
                guess1=str(input(">"))
                if(guess1 in words.MediumWordscomplete):
                    print("\nCorrect ✅.")
                    M_Score+=5/2
                    continue
                else:
                    print("\nWrong guess❌")
                    continue
            print("==================")
            print(f"\nYou Scored {M_Score}%.")
            print("PlayAgain? (Y/N)")
            prompt1=str(input(">")).lower()
            if(prompt1==("y")):
                WordGuess()
            elif(prompt1==("n")):
                print("\nThanks For Playing.👋")
                sys.exit()
            print("==================")
            sys.exit()
        
        def Hard():
            H_Score=0
            print("\nDifficulty : HARD")
            for ou in range(5):
                print("Guess the Word")
                print(random.choice(words.HardWordsblank))
                guess1=str(input(">"))
                if(guess1 in words.HardWordscomplete):
                    print("\nCorrect ✅.")
                    H_Score+=5/2
                    continue
                else:
                    print("\nWrong guess❌")
                    continue
            print("==================")
            print(f"\nYou Scored {H_Score}%.")
            print("PlayAgain? (Y/N)")
            prompt2=str(input(">")).lower()
            if(prompt2==("y")):
                WordGuess()
            elif(prompt2==("n")):
                print("\nThanks For Playing.👋")
                sys.exit()
            print("==================")
            sys.exit()
        
        def Extreme():
            Ex_Score=0
            print("\nDifficulty : EXTREME")
            for ou in range(5):
                print("Guess the Word")
                print(random.choice(words.ExtremeWordsblank))
                guess1=str(input(">"))
                if(guess1 in words.ExtremeWordscomplete):
                    print("\nCorrect ✅.")
                    Ex_Score+=5/2
                    continue
                else:
                    print("\nWrong guess❌")
                    continue
            print("==================")
            print(f"\nYou Scored {Ex_Score}%.")
            print("PlayAgain? (Y/N)")
            prompt3=str(input(">")).lower()
            if(prompt3==("y")):
                WordGuess()
            elif(prompt3==("n")):
                print("\nThanks For Playing.👋")
                sys.exit()
            print("==================")
            sys.exit()
    except ValueError:
        print("ERROR: Not Allowed🚫.")
        sys.exit()

    Mainc()
WordGuess()