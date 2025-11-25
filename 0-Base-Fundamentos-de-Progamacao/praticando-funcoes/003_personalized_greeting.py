def personalized_greeting(current_time: int):
    if current_time < 12:
        return "Good Morning!"
    elif current_time < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"


current_time = int(input("Type the current hour(0-23): "))
print(personalized_greeting(current_time))
