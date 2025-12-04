class Music:
    musics = []

    def __init__(self, name: str, artist: str, duration: float):
        self.name = name
        self.artist = artist
        self.duration = duration
        Music.musics.append(self)

    def __str__(self):
        return f"song: {self.name} | artist: {self.artist} | duration: {self.duration} minutes."

    def show_musics():
        for music in Music.musics:
            print(music)


music1 = Music("Me and Bob McGee", "Janis Joplin", 4.32)
music2 = Music("What's Up", "4 Non Blonds", 4.53)
music3 = Music("Ode To My Family", "The Cranberries", 4.33)

print(music1)

Music.show_musics()
