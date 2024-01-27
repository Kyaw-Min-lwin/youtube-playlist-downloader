from pytube import Playlist
import tkinter as tk
from tkinter import filedialog
from pprint import pprint
def download_playlist(playlist, save_path):
    try:
        # creating the playlist object
        p = Playlist(playlist)
        print(p)

        for video in p.videos:
            print(video)
            # filtering by progressive means both video and audio in one file
            streams = video.streams.filter(file_extension='mp4', progressive=True)
            print(streams)
            # getting the highest resolution
            highest_resolution = streams.get_highest_resolution()
            # downloading the highest resolution video
            highest_resolution.download(output_path=save_path)
    except Exception as e:
        print(e)

def choose_folder():
    folder = filedialog.askdirectory()
    if folder:
        print(f'You chose {folder} folder')
    return folder

if __name__ == '__main__':
    root = tk.Tk()
    root.withdraw()

    playlist_url = input('Please input the url of a playlist : ')
    save_dir = choose_folder()

    if save_dir:
        print('download started')
        download_playlist(playlist_url, save_dir)
    else:
        print('Invalid saved directory')