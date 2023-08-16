import requests
import re
import sys

#Created by gutierre0x80

RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

def playlist_exists(html_content):
    return 'href="' in html_content and '/playlist?list=' in html_content

def get_playlist_duration(html_content):
    durations = re.findall(r'"simpleText":"(\d+:\d+)"', html_content)

    total_duration_seconds = 0
    for duration in durations:
        minutes, seconds = map(int, duration.split(":"))
        total_duration_seconds += (minutes * 60 + seconds) / 2

    total_hours = total_duration_seconds // 3600
    total_minutes = (total_duration_seconds % 3600) // 60
    total_seconds = total_duration_seconds % 60

    return total_hours, total_minutes, total_seconds

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{RED}Usage: python program_name.py playlist_url{RESET}")
        sys.exit(1)

    playlist_url = sys.argv[1]
    if not playlist_url.startswith("https://www.youtube.com/playlist?list="):
        print(f"{RED}Invalid playlist URL. Please provide a valid YouTube playlist URL.{RESET}")
        sys.exit(1)

    response = requests.get(playlist_url)
    html_content = response.text

    if not playlist_exists(html_content):
        print(f"{RED}Playlist does not exist.{RESET}")
        sys.exit(1)

    hours, minutes, seconds = get_playlist_duration(html_content)

    print(f"Duration of the playlist: {GREEN}{hours} hours, {minutes} minutes, {seconds} seconds{RESET}")
