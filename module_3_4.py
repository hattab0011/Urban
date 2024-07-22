def single_root_words(root_world, *other_worlds):
    same_words = []
    for word in other_worlds:
        if root_world in word:
            same_words.append(word)
    print(same_words)


single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')