from bs4 import BeautifulSoup
import requests
from ytmusicapi import YTMusic

import os

if not os.path.exists("browser.json"):
    print("browser.json not found.")
    print("You need to authenticate with YouTube Music first.")
    print("Run one of these commands in your terminal from this project folder:\n")
    print("  Mac:     pbpaste | ytmusicapi browser")
    print("  Windows: ytmusicapi browser\n")
    print("Copy the request headers from Firefox first.")
    print("This will create browser.json.")
    exit()

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36"}
date = input("Which year do you want to travel to?Type the date in this format YYYY-MM-DD: ")
response = requests.get(url=f"https://appbrewery.github.io/bakeboard-hot-100/{date}/", headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")

music_list = soup.find_all(name="h3", class_="chart-entry__title")
song_names = [song.getText().strip() for song in music_list]


yt = YTMusic("browser.json")

PLAYLIST_NAME = f"{date} Billboard 100"
playlist_id = None
playlists = yt.get_library_playlists(limit=100)

for p in playlists:
    if p["title"] == PLAYLIST_NAME:
        playlist_id = p["playlistId"]
        break


if playlist_id:
    print("This playlist already exists.")
else:
    playlist_id = yt.create_playlist(
        PLAYLIST_NAME,
        f"Playlist with the hottest songs from {date}",
        privacy_status="PRIVATE",
    )
    print("Playlist created.")

for song in song_names:
    try:
        search_result= yt.search(
            query=song,
            filter="songs",
        )
        video_id = search_result[0]["videoId"]
        yt.add_playlist_items(
            playlistId=playlist_id,
            videoIds=[video_id]
        )
        print(f"Added: {song}")
    except Exception as e:
        print(f"Skipped: {song} | Reason: {e}")