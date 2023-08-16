import requests
import re
import sys

def get_playlist_duration(playlist_url):
    response = requests.get(playlist_url)
    html_content = response.text

    durations = re.findall(r'"simpleText":"(\d+:\d+)"', html_content)

    total_duration_seconds = 0
    for duration in durations:
        minutes, seconds = map(int, duration.split(":"))
        total_duration_seconds += minutes * 60 + seconds

    total_hours = total_duration_seconds // 3600
    total_minutes = (total_duration_seconds % 3600) // 60
    total_seconds = total_duration_seconds % 60

    return total_hours, total_minutes, total_seconds

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python program_name.py playlist_url")
        sys.exit(1)

    playlist_url = sys.argv[1]
    if not playlist_url.startswith("https://www.youtube.com/playlist?list="):
        print("Invalid playlist URL. Please provide a valid YouTube playlist URL.")
        sys.exit(1)

    hours, minutes, seconds = get_playlist_duration(playlist_url)

    print(f"Duration of the playlist: {hours} hours, {minutes} minutes, {seconds} seconds")
