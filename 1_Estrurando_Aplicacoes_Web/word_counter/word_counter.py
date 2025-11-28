# # 1- Initial CODE

# phrase = input("Type a phrase: ")
# words = phrase.split()
# print(len(words))
# print(words)

# 2- Improving the CODE using function


# def word_counter(phrase):
#     words = phrase.split()
#     print(words)
#     return len(words)


# 3- Improving the CODE
# -> Process the sentence to remove punctuation
# -> Convert the words to lowercase


# def clear_text(text):
#     text = text.lower()
#     characters = ",.!|?;:\"'()[]{}/"
#     for character in characters:
#         text = text.replace(character, "")

#     return text


# def word_counter(phrase):
#     phrase = clear_text(phrase)
#     words = phrase.split()
#     return len(words)


# 4- Improving the CODE
# -> dictionary to store the frequency of words and avoid invalid entries


def clear_text(text):
    text = text.lower()
    characters = ",.!|?;:\"'()[]{}/-"
    for character in characters:
        text = text.replace(character, "")

    return text


def word_counter(phrase):
    phrase = clear_text(phrase)
    if not phrase.strip():
        return {}
    words = phrase.split()
    counter = {}
    for word in words:
        # Increments the count for this word,get(word, 0) starting at 0 if the word is not in the dictionary
        counter[word] = counter.get(word, 0) + 1
    return counter
