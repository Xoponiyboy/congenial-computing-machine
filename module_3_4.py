def single_root_words(root_word, *other_word):
    same_words = []
    for Jmix in other_word:
        a, b = (root_word.upper(), Jmix.upper())
        if a in b or b in a:
            same_words.append(Jmix)
    return same_words
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)