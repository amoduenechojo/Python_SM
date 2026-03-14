list_of_words = ["lamb", "kit", "kings", "dogs", "man"]
def character_above_three(list_of_words):
    empty_string = []

    for word in list_of_words:
        if len(word) > 3:
            empty_string.append(word)
    return empty_string

            
