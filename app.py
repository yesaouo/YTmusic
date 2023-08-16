import os, json, yt_dlp
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)

song_dict = {}
json_file_path = 'song_data.json'
if os.path.exists(json_file_path):
    with open(json_file_path, 'r', encoding="utf-8") as json_file:
        song_dict = json.load(json_file)

def replace_invalid_characters(input_string):
    invalid_characters = [' ', '<', '>', '#', '%', '{', '}', '|', '\\', '^', '~', '[', ']', '`']
    filtered_string = ''.join(['_' if char in invalid_characters else char for char in input_string])
    return filtered_string

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/add_song', methods=['POST'])
def add_song():
    global song_dict
    video_url = request.form['text']
    if not song_dict.get(video_url):
        ydl = yt_dlp.YoutubeDL()
        try:
            video_info = ydl.extract_info(video_url, download=False)
            video_title = video_info.get('title', None)
            if video_title:
                video_title = replace_invalid_characters(video_title)
                os.system(f'yt-dlp -o "static/{video_title}.m4a" -x --audio-format m4a {video_url}')
                song_dict[video_url] = video_title
                with open(json_file_path, 'w', encoding="utf-8") as json_file:
                    json.dump(song_dict, json_file)
        except:
            pass
    return jsonify({'dict': song_dict})

@app.route('/remove_song', methods=['POST'])
def remove_song():
    global song_dict
    video_title = request.form['text']
    filePath = f'static/{video_title}.m4a'
    if os.path.exists(filePath):
        os.remove(filePath)
    song_dict = {key: value for key, value in song_dict.items() if value != video_title}
    with open(json_file_path, 'w', encoding="utf-8") as json_file:
        json.dump(song_dict, json_file)
    return jsonify({'dict': song_dict})

@app.route('/get_song_list', methods=['GET'])
def get_song_list():
    return jsonify({'dict': song_dict})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
