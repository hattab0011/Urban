def single_root_words(root_world, *other_worlds):
    same_words = []
    root_world_lower = root_world.lower()
    for word in other_worlds:
        if root_world_lower in word.lower() or word.lower() in root_world_lower:
            same_words.append(word)
    return (same_words)

result = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result)