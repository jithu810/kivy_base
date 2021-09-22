
from kivy.app import App
from kivy.uix.video import Video
from kivy.uix.widget import Widget
 
 
 
class VideoWindow(App):
    def build(self):
 
        video = Video(source='Lucifer_S04E08.mkv',state='play')
        
        return video
 
 
 
 
if __name__ == "__main__":
    window = VideoWindow()
    window.run()