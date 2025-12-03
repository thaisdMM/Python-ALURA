class Music:
    name = ""
    artist = ""
    duration = float


music1 = Music()
music1.name = "Me and Bob McGee"
music1.artist = "Janis Joplin"
music1.duration = 4.32


music2 = Music()
music2.name = "What's Up"
music2.artist = "4 Non Blonds"
music2.duration = 4.53

music3 = Music()
music3.name = "Ode To My Family"
music3.artist = "The Cranberries"
music3.duration = 4.33


print(vars(music1))
print(vars(music2))
print(vars(music3))

# 2
music4 = Music()
music4.name = "Bohemian Rhapsody"
music4.duration = 355

print(f"Music: {music4.name} - Artist: {music4.artist} - {music4.duration} seconds")
