import youtube_dl
from bs4 import BeautifulSoup
import requests
from os import chdir
from utilities.dataRetreiver import base_path

ydl_opts = {
    'ffmpeg_location': base_path + '/utilities/ffmpeg',
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192'
    }]
}


def search_for_song(song_title):
    formatted_title = '+'.join(song_title).lower()
    base_url = 'https://www.youtube.com'
    search_ext = '/results?search_query='
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) '
                             'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    # Class of the first video result
    first_result = "yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "

    raw_text = requests.get(base_url + search_ext + formatted_title, headers=headers)
    soup = BeautifulSoup(raw_text.text, 'lxml')
    search_result = soup.find('a', {'class': first_result})
    watch_ext = search_result.get('href')
    return base_url + watch_ext


def process(user_input):
    music_location = base_path + '/data/musicTemp'
    youtube_url = search_for_song(user_input)
    chdir(music_location)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print(ydl.download([youtube_url]))
    return music_location
