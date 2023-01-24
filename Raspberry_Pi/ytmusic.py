from pytube import Playlist
from pytube import YouTube
import os
import sys

try:    mode = sys.argv[1]
except: mode = '1'
try:    path = sys.argv[2]
except: path = './Music'
try:    URL  = sys.argv[3]
except: URL  = ''

#html
htmlfront = ''
htmlback  = ''

def getFilelist():
  try: os.makedirs(path)
  except FileExistsError: pass
  return os.listdir(path)

def downloadMovie(url = URL):
  try:
    files = getFilelist()
    yt = YouTube(url)
    title = yt.title.replace('/','').replace("'",'').replace('"','').replace('.','')
    title = f'{title}.mp3'
    if title not in files:
      yt = yt.streams.filter(only_audio=True, bitrate='128kbps', abr='128kbps').first()
      out_file = yt.download(output_path=path)
      base, ext = os.path.splitext(out_file)
      new_file = base + '.mp3'
      os.rename(out_file, new_file)
      print('Download completed.')
    else:
      print('Already downloaded.')
  except Exception as e: print(e)

def downloadPlaylist():
  try:
    playlist = Playlist(URL)
    if len(playlist) == 0:
      print('Downloading...')
      downloadMovie(URL)
    else:  
      for video in playlist:
        print('Downloading...')
        downloadMovie(video)
      print('All files downloaded.')
    buildHTML()
  except: 
    downloadMovie()
    buildHTML()

def buildHTML():
  try:
    global htmlfront, htmlback
    htmlmiddle = ''
    files = getFilelist()
    for file in files:
      htmlmiddle += '<li data-src="' + path + '/' + file + """" onmousedown="holdDown('""" + path + '/' + file + """')" onmouseup="holdUp()">""" + file.replace(".mp3","") + '</li>'
    html = htmlfront + htmlmiddle + htmlback
    fout = open("index.html", "w", encoding='UTF-8')
    fout.write(html)
    fout.close()
    print('Build complete.')
  except Exception as e: print(e)

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
    form {
    display: flex;
    flex-wrap: wrap;
    }
    #url{
    flex-grow: 1;
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
    <form method="POST" action="index.php" />
      URL:
      <input type="text" name="url" id="url" placeholder="https://www.youtube.com/"/>
      <input type="submit" value="Download" name="download" />
      <input type="hidden" name="folder-path" id="folder-path" value="./Music" />
    </form>
  </div>
  <form id="delete" method="POST" action="index.php" />
    <input type="hidden" name="path" id="path" />
    <input type="hidden" name="file-path" id="file-path">
  </form>

<script>
//onsubmit="document.getElementById('folder-path').value = path;"
//<input type="button" value="Set Path" id="set-path" />
/*
  if (!localStorage.getItem('music-path')) {
    localStorage.setItem('music-path','./Music');
  }
  let path = localStorage.getItem('music-path');
  let setPath = document.getElementById('set-path');
  setPath.onclick = function() {
    let pathTemp = window.prompt('Set music location.',path);
    if (pathTemp) {
      path = pathTemp;
      localStorage.setItem('music-path',path);
    }
  };
*/
  let path = './Music';
</script>
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
      nowPlay.innerHTML = 'Now Playing: ' + songSrc.replace(path + '/','').replace('.mp3','')
    }
  });
</script>
<script>
  var timeStart, timeEnd, time;
  function getTimeNow() {
    var now = new Date();
    return now.getTime();
  }
  function holdDown(filePath) {
    timeStart = getTimeNow();
    time = setInterval(() =>{
      timeEnd = getTimeNow();
      if(timeEnd - timeStart > 1000) {
        clearInterval(time);
        if(window.prompt('Are you sure you want to delete this music?','yes') == 'yes'){
          document.getElementById('path').value = path;
          document.getElementById('file-path').value = filePath;
          document.getElementById('delete').submit();
        }
      }
    }, 100);
  }
  function holdUp() {
    clearInterval(time);
  }
</script>
</body>
</html>
"""

if mode == '1':
  downloadPlaylist()
elif mode == '2':
  buildHTML()
