import time
import vlc

class BasePlayer():
    def __init__(self) -> None:
        pass

    def play(self):
        # creating vlc media player object
        p2_player = vlc.MediaPlayer("./data/sounds/Alarm-Fast-A1-www.fesliyanstudios.com.mp3")

        p2_player.play()
        #hack
        time.sleep(0.3)
        
        duration = p2_player.get_length()/1000
        time.sleep(duration)

class Player(BasePlayer):
    def __init__(self) -> None:
        super().__init__()

    def play(self, audio_path):
        super().play()
        
        p3_player = vlc.MediaPlayer(audio_path)

        p3_player.play()
        #hack
        time.sleep(0.3)
        
        duration = p3_player.get_length()/1000
        time.sleep(duration)
        p3_player.stop()

if __name__ == "__main__":
    # player = BasePlayer()
    # player.play()

    player = Player()
    player.play("./data/sounds/The_Renegade.mp4")
    