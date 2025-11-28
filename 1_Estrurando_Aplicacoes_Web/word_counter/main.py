from word_counter import word_counter

# 1- first CODE
#
# phrase = input("Type a phrase: ")
# number_of_words = word_counter(phrase)
# print(f"The phrase has {number_of_words} words.")

# 2- Improving the CODE
# -> Check if the input is empty
# -> Display the word count clearly

phrase = input("Type a phrase: ").strip()
if not phrase:
    print("Error: no sentece was typed")
else:
    result = word_counter(phrase)
    if result:
        print("Word count:")
        for word, counter in result.items():
            print(f"{word}: {counter}")
    else:
        print(f"No valid word was found.")
