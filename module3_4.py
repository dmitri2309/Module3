def single_root_words(*other_word, root_word):
    same_words = []
    for i in other_word:
        #if root_word.upper() in [j.upper() for j in other_word]:
        n = i.upper()
        b = root_word.upper()
        if b in n or n in b:
            same_words.append(i)
    return same_words
result1 = single_root_words('richiest', 'orichalcum', 'cheers', 'richies',root_word ='rich')
print(result1)
result2 = single_root_words('Able', 'Mable', 'Disable', 'Bagel',root_word = "disablement")
print(result2)

