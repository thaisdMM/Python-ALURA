# 1- first option

user_input = input("Type the numbers separeted by spaces: ").split()
converted_number = [int(value) for value in user_input]
even_list = list(filter(lambda x: x % 2 == 0, converted_number))

# convert_str = [str(value) for value in even_list]
# result = " ".join(convert_str)

# simpler
result = " ".join(map(str, even_list))

print(f"Even numbers: {result}")

# 2- other way:
# CODE FOR STUDY REFERENCE: FILTERING AND LAZY EVALUATION

user_input = input("Type the numbers separeted by spaces: ").split()

# 2. Apply the filter() function.
# The filter() function returns a LAZY ITERATOR object, not a list.
# even_list only contains the "recipe" for filtering, not the results yet.
even_list = filter(lambda x: int(x) % 2 == 0, user_input)

# 3. Output the results using the efficient join() method.
# The join() method can consume the ITERATOR (even_list) directly.
# This processes the numbers ONE BY ONE ("on demand") without creating a full intermediate list,
# saving memory, especially for large datasets (lazy evaluation).
print("Even numbers:", " ".join(even_list))
