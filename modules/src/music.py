import youtube_dl
from bs4 import BeautifulSoup
import requests
from os import chdir

ydl_opts = {
    'ffmpeg_location': 'C:/Users/Ethan/Documents/GitHub/Box-Bot/utilities/ffmpeg',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }]
}


def search_for_song(song_title):
    base_url = 'https://www.youtube.com/'
    search_addon = 'results?search_query='
    video_addon = 'watch?v=_ZxJPOqLZqQ'
    raw_text = requests.get(base_url + search_addon + song_title)



def process(user_input):
    youtube_url = search_for_song(user_input)
    chdir(r'C:\Users\Ethan\Documents\GitHub\Box-Bot\data\musicTemp')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print(ydl.download(['https://www.youtube.com/watch?v=V_cVzQY1YgI']))

search_for_song('Haley steinfield starving')