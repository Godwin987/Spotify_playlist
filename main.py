import requests
import os
import spotipy
from pprint import pprint
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

load_dotenv('cred.env')
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
REDIRECT_URL = os.getenv('REDIRECT_URL')
scope = os.getenv('scope')
USER_ID = os.getenv('USER_ID')
PLAYLIST_ID = os.getenv('PLAYLIST_ID')
TOKEN = os.getenv('TOKEN')
LIBRARY_ID = os.getenv('LIBRARY_ID')


date = input("What year would you like to travel to (YYYY-MM-DD): ")
URL = "https://www.praisecharts.com/api/elastic/song-list/top-100-contemporary-hymns-of-2020"

querystring = {"token": TOKEN, "libraryId": LIBRARY_ID}

payload = ""
headers = {
    "authority": "www.praisecharts.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9"
                     ".eyJNZW1iZXJJRCI6MTIzNDgyOCwic3ViIjoxMjM0ODI4LCJpc3MiOiJodHRwczovL3d3dy5wcmFpc2Vj"
                     "aGFydHMuY29tL3BjNS9hdXRoZW50aWNhdGUiLCJp"
                     "YXQiOjE2NzA2NzE3NTgsImV4cCI6MTY3MzI2Mzc1OCwibmJmIjoxNjcwNjcxNzU4LCJqdGkiOiJMR0VPd"
                     "lc2WWNGYVJXR1lQIn0._YGZ3Ea_WNKDi9"
                     "jMxzE1QFkgBxePxnQ5c4ee3QEHdg",
    "cookie": "_ga=GA1.2.576965885.1669592231; _hjSessionUser_744555=eyJpZCI6IjZlNDQ3MGRkLWY2YTAtNTI2MC04MmE1LThmYjQ5N"
              "DEyMTBkZiIsImNyZWF0ZWQiOjE2Njk1OTIyMzI0OTIsImV4aXN0aW5nIjp0cnVlfQ==; G_ENABLED_IDPS=google; _gid=GA1."
              "2.1538216333.1670535948; trustedsite_visit=1; UserLanguageCode=en-US; mktz_client=^%^7B^%^22is_returning"
              "^%^22^%^3A0^%^2C^%^22uid^%^22^%^3A^%^22140114071148572073^%^22^%^2C^%^22"
              "session^%^22^%^3A^%^22sess.2.4138"
              "961853.1670626751027^%^22^%^2C^%^22views^%^22^%^3A1^%^2C^%^22referer_url^%^22^%^3A^%^22https^%^3A//www.b"
              "ing.com/^%^22^%^2C^%^22referer_domain^%^22^%^3A^%^22www.bing.com^%^22^%^2C^%^22referer_type^%^22^%^3A^%^"
              "22organic^%^22^%^2C^%^22visits^%^22^%^3A1^%^2C^%^22landing^%^22^%^3A^%^22https^%^3A//www.praisecharts.co"
              "m/company/praisecharts-api-usage-agreement/^%^22^%^2C^%^22enter_at^%^22^%^3A^%^222022-12-9^%^7C23^%^3A59"
              "^%^3A11^%^22^%^2C^%^22first_visit^%^22^%^3A^%^222022-12-9^%^7C23^%^3A59^%^3A11^%^22^%^2C^%^22last_visit^"
              "%^22^%^3A^%^222022-12-9^%^7C23^%^3A59^%^3A11^%^22^%^2C^%^22last_variation^%^22^%^3A^%^22^%^22^%^2C^%^22u"
              "tm_source^%^22^%^3Afalse^%^2C^%^22utm_term^%^22^%^3Afalse^%^2C^%^22utm_campaign^%^22^%^3Afalse^%^2C^%^2"
              "2utm_content^%^22^%^3Afalse^%^2C^%^22utm_medium^%^22^%^3Afalse^%^2C^%^22consent^%^22^%^3A^%^22^%^22^%^7"
              "D; _fbp=fb.1.1670626753079.1970575692; _omappvp=bAOPI0gwh4MSL6mNIeX5IZC5MY22vgL9oCEZK2ku4AWs3h6q6p1n3"
              "2HfiQCL73NSoYlW7M7uGVrOQmBOWaKgSROfxlWB0qaG; UserToken=7b36f6a0f237d26646779a078d343129; UserApiToken=e"
              "yJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJNZW1iZXJJRCI6MTIzNDgyOCwic3ViIjoxMjM0ODI4LCJpc3MiOiJodHRwczovL3"
              "d3dy5wcmFpc2VjaGFydHMuY29tL3BjNS9hdXRoZW50aWNhdGUiLCJpYXQiOjE2NzA2NzE3NTgsImV4cCI6MTY3MzI2Mzc1OCwibmJm"
              "IjoxNjcwNjcxNzU4LCJqdGkiOiJMR0VPdlc2WWNGYVJXR1lQIn0._YGZ3Ea_WNKDi9ujMxzE1QFkgBxePxnQ5c4ee3QEHdg; _hjS"
              "ession_744555=eyJpZCI6IjM2MmM3YjY4LWYwYzItNGU3ZC1hYTBjLWRhMTQ3YTY2MTI2NyIsImNyZWF0ZWQiOjE2NzA2NzE3NjI"
              "0ODAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0",
    "referer": "https://www.praisecharts.com/song-lists/top-100-contemporary-hymns-of-2020",
    "sec-ch-ua": "^\^Not?A_Brand^^;v=^\^8^^, ^\^Chromium^^;v=^\^108^^, ^\^Microsoft",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "^\^Windows^^",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 "
                  "Safari/537.36 Edg/108.0.1462.42 "
}

response = requests.request("GET", URL, data=payload, headers=headers, params=querystring)

data = response.json()

new_songs = [song["details"]["catalog_item_title"] for song in data["songs"]]

# response = requests.get(URL)
# billboard_html = response.text
#
# soup = BeautifulSoup(billboard_html, "html.parser")
#
# all_songs = soup.select(selector="li ul li h3", id="title-of-a-story")
# songs = [songs.get_text().strip("\n\t") for songs in all_songs]

# login to spotify
spotify = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
                       redirect_uri=REDIRECT_URL, scope=scope, cache_path="token.txt")

token = spotify.get_access_token(as_dict=True)
user = spotipy.Spotify(auth=token["access_token"])
current_user = user.current_user()["id"]
# print(current_user)
spotify.get_cached_token()

year = date.split("-")[0]
song_uris = []

# searching spotify for the song uri's
for song in new_songs:
    result = user.search(q=f"track:{song} year:{year}", type="track")
    # pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist_name = f"{date} Billboard 100"
#
# playlist_create = user.user_playlist_create(user=USER_ID, name=playlist_name, public=False)
# # print(playlist_create)
# playlist_id = playlist_create["id"]
# print(playlist_id)

# replace songs
user.playlist_replace_items(playlist_id=PLAYLIST_ID, items=song_uris)
