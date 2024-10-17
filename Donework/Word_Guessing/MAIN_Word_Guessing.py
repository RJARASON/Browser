try:
    import sys
    print("=================")
    print("Word Guessing Game")
    print("\nSelect level")
    print("WG 1")
    print("WG 2")
    select=str(input(">")).lower()
    if(select==("wg 1") or select==("wg1")):
        import Word_Guess1   
    elif(select==("wg 2") or select==("wg2")):
        import Word_Guess2    
    else:
        print("\nERROR: please select level.")
        sys.exit()
except Exception:
    print("\nERROR: Not Allowed.")
    sys.exit()