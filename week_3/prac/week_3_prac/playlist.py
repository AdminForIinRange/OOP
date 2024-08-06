import random

class Playlist:
    def __init__ (self, name, current_song):
        self.name = name
        self.songs = []
        self.current_song = current_song
        self.shuffling = False
        self.next_index = 0
        
    def add_song (self, song):
        if song in self.songs:
            print(f"{song} is already in the list")
        else:   
            self.songs.append(song)
            print(f"{song} is has been added")
        
    def remove_song (self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"{song} has been removed")
        else:   
            print(f"{song} is not in the list")
        
    def shuffling_song (self):
        print("track has been shuffled")
        self.shuffling = True
        self.next_index = 0
        
    def play (self):
        if not self.shuffling: # not is just false like in js
            print(f"{self.current_song} is playing")
        else:
            index = random.randint(0, len(self.songs)-1)
            self.current_song = self.songs[index]
            self.next_index = index + 1
            print(f"{self.current_song} is playing")
        
    def next_track (self):
        if self.next_index < len(self.songs):
            self.current_song = self.songs[self.next_index]
            self.next_index += 1
            print("playing next song")
        else:
            print(f"sorry no songs after {self.current_song}")
             index = random.randint(0, len(self.songs)-1)    

Playlist1 = Playlist("Playlist1", "current_song")
Playlist1.add_song("song1")
Playlist1.add_song("song2")
Playlist1.add_song("song3")
Playlist1.remove_song("song3")

Playlist1.shuffling_song()

Playlist1.play()
Playlist1.next_track()
Playlist1.back_track()
Playlist1.play()





        

