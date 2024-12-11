import pygame

class Music:
    
    def __init__(self, music_file):
        """
        Initializes the Music class and starts playing the background music.
        
        args:
        - music_file (str): path to the music file (e.g., "background_music.mp3")
        """
        pygame.mixer.init()
        
        self.music_file = music_file 
         
        self.play_music()  

    def play_music(self):
        """
        Plays the background music in a loop.
        """
        try:
            pygame.mixer.music.load(self.music_file)  
            
            pygame.mixer.music.play(-1) 
            
        except pygame.error as e:
            
            print(f"Error loading music file: {e}")

    def stop_music(self):
        """
        Stops the background music.
        """
        pygame.mixer.music.stop()
        
        print("Music stopped.")
        
