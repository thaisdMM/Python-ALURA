from datetime import date


def calculate_age(year_of_birth, current_year):
    return current_year - year_of_birth


year_of_birth = int(input("Year of birth: "))
current_year = date.today().year
age = calculate_age(year_of_birth, current_year)
print(f"The age is {age} years.")
