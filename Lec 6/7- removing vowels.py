def remove_vowels():
    word = input("please enter a word: ")
    no_vowel = ''
    for ch in word:
        if ch in 'aoei':
            continue
        else:
            no_vowel = no_vowel + ch
    print(no_vowel)

remove_vowels()
