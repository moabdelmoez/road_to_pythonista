def char_count(word, char):
    "count characters in a specific word"
    count = 0
    for letter in word:
        if letter == char:
            count = count + 1
    print(count)

char_count("mostafa", 'a')
char_count("garger", 'g')
        
