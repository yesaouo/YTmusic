from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from pytube import Playlist
from pytube import YouTube
import webbrowser
import os

#html
htmlfront = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MusicPlayer</title>
  <style>
      html, body {
      background-color: #f1faee;
      width: 100%;
      padding: 0;
      margin: 0;
      }
      audio {
      width: 100%;
      }
      li {
      border-bottom: 1px solid #457b9d;
      }
      #song-list {
      margin: 0 auto;
      }
      #song-list ul {
      list-style-type: none;
      }
      #song-list li {
      padding: 5px;
      cursor: pointer;
      }
      #song-list li:hover {
      background-color: #f0f0f0;
      color: #e63946;
      }
      #pos-fixed {
      background-color: #1d3557;
      color: white;
      width: 90%;
      position: fixed;
      bottom: 3%;
      left: 3%;
      padding: 1% 2%;
      border-radius: 10px;
      }
      #now-play {
      overflow: hidden;
      white-space: nowrap;
      }
  </style>
</head>
<body>
<div id="song-list">
  <ol>
"""
htmlback = """
  </ol>
</div>

<div id="pos-fixed">
  <div id="now-play"></div>
  <audio id="player" controls loop></audio>
</div>

<script>
const player = document.getElementById("player");
const songList = document.getElementById("song-list");
const nowPlay = document.getElementById("now-play");

songList.addEventListener("click", (event) => {
  if (event.target.tagName === "LI") {
    const songSrc = event.target.getAttribute("data-src");
    player.src = songSrc;
    player.volume = 0.5;
    player.play();
    nowPlay.innerHTML = 'Now Playing: ' + songSrc.replace('./Music/','').replace('.mp3','')
  }
});
</script>
</body>
</html>
"""

class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.cols = 1
        self.add_widget(Button(text='Download the Video / Playlist', on_press=self.option1_callback))
        self.add_widget(Button(text='Open the Music Player', on_press=self.option2_callback))
        self.input = TextInput(multiline=False, on_text_validate=self.send_callback, size_hint_y=None, height=30)
        self.add_widget(self.input)
        self.output_label = Label(text='Pass the URL in the input box above.', size_hint_y=None, height=30)
        self.add_widget(self.output_label)

    def option1_callback(self, instance):
        if self.input.text == '':
          self.output_label.text = 'Pass the URL in the input box above.'
        else:
          self.output_label.text = 'Checking the URL...'
          self.downloadPlaylist(self.input.text)

    def option2_callback(self, instance):
        self.buildHTML()
        self.output_label.text = 'Music player opens in a new window.'

    def send_callback(self, instance):
        self.output_label.text = 'URL: '+ instance.text

    def getFilelist(self):
      folder_path = './Music'
      try:
        os.makedirs(folder_path)
      except FileExistsError:
        pass
      return os.listdir(folder_path)

    def downloadMovie(self, URL):
      try:
        files = self.getFilelist()
        yt = YouTube(URL)
        title = yt.title.replace('/','').replace("'",'').replace('"','').replace('.','')
        title = f'{title}.mp3'
        if title not in files:
          yt = yt.streams.filter(only_audio=True, bitrate='128kbps', abr='128kbps').first()
          out_file = yt.download(output_path='./Music')
          base, ext = os.path.splitext(out_file)
          new_file = base + '.mp3'
          os.rename(out_file, new_file)
          self.output_label.text = 'Download completed.'
        else:
          self.output_label.text = 'Already downloaded.'
      except:
        self.output_label.text = 'Something went wrong.'

    def downloadPlaylist(self, URL):
      try:
        self.output_label.text = 'Downloading...'
        playlist = Playlist(URL)
        if len(playlist) == 0:
          self.downloadMovie(URL)
        else:  
          for video in playlist:
            self.downloadMovie(video)
          self.output_label.text = 'All files downloaded.'
      except:
        self.downloadMovie(URL)

    def buildHTML(self):
      try:
        global htmlfront, htmlback
        htmlmiddle = ''
        files = self.getFilelist()
        for file in files:
          htmlmiddle += f'<li data-src="./Music/{file}">{file.replace(".mp3","")}</li>'
        html = htmlfront + htmlmiddle + htmlback
        fout = open("YTmusic.html", "w", encoding='UTF-8')
        fout.write(html)
        fout.close()
        self.output_label.text = 'Build complete.'
        webbrowser.open("YTmusic.html")
      except:
        self.output_label.text = 'Something went wrong.'

class MyApp(App):
    def build(self):
        self.icon = 'icon.png'
        self.title = 'YTmusic'
        return MyLayout()

if __name__ == '__main__':
    MyApp().run()
