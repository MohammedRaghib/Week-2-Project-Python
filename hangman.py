def hangman():
    import random

    tries = 6
    tried = set()
    r_tried = set()
    list_of_words = ["Coding", "Variable", "Function", "Module", "Import", "Loop", "List", "Dictionary", "Tuple", "String", "Integer", "Boolean", "Class", "Object", "Syntax", "Indentation", "Library", "Decorator", "Parameter", "Argument"]

    random_choice = random.choice(list_of_words).lower()
    dashed_word = ['_'] * len(random_choice)

    print(f'Lets play hangman: Word is {' '.join(dashed_word)}' )

    while tries > 0:
        if set(random_choice) == r_tried:
            print(f'Congrats the word is found: {random_choice}')
            break
        else:
            inp = str(input('Enter a letter: ')).lower()
            if len(inp) == 1 and inp.isalpha():
                if inp in random_choice:
                    if inp in r_tried:
                        print('Already tried that letter')
                    else:
                        r_tried.add(inp)
                        for idx, letter in enumerate(random_choice):
                            if letter == inp:
                                dashed_word[idx] = inp
                        print(' '.join(dashed_word))
                else:
                    if inp in tried:
                        print('Already tried that letter')
                        tries -= 1
                    else:
                        tried.add(inp)
                        tries -= 1
                        print(f'Wrong letter, {tries} tries left')
            else:
                print('One letter only')
    else:
        print(f'Sorry you lost, the word was {random_choice.upper()}')
hangman()
                