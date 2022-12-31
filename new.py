# import os
# from contextlib import closing
# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.edge.service import Service
# from selenium.webdriver.edge.options import Options
# import requests
# from bs4 import BeautifulSoup
#
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# chrome_service = Service(executable_path="chromedriver.exe")
# driver = webdriver.Chrome(options=options, service=chrome_service)
#
# parameters = {
#     "limit": 100,
# }
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 "
#                   "Safari/537.36 Edg/108.0.1462.42",
#     "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJNZW1iZXJJRCI6MTIzNDgyOCwic3"
#                      "ViIjoxMjM0ODI4LCJpc3MiOiJodHRwczovL3d3dy5wcmFpc2VjaGFydHM"
#                      "uY29tL3BjNS9hdXRoZW50aWNhdGUiLCJpYXQiOjE2Nz "
#                      "A2MjcwNTEsImV4cCI6MTY3MzIxOTA1MSwibmJmIjoxNjcwNjI3MDUxLCJqdGkiOiJJRTFEZGFHeURYMmRNbWpyIn0"
#                      ".ITUwzCUTGOzs-0p3KTqdo9EhQNkI0xsEpK9HxCkGmOA",
#     "Referer": "https://www.praisecharts.com/song-lists/top-100-contemporary-hymns-of-2020",
#     "Accept": "application/json, text/plain, */*"
# }
#
# response = requests.get("https://praisecharts.com/song-lists/top-100-contemporary-hymns-of-2020",
#                         params=parameters, headers=headers)
#
# html = response.text
# # songs = driver.find_elements(By.CLASS_NAME, "text-white m-0 text-truncate")
# # # print(len(songs))
# # for song in songs:
# #     print(song.text)
#
# page = driver.get("https://praisecharts.com/song-lists/top-100-contemporary-hymns-of-2020?limit=100")
# button = driver.find_element(By.XPATH, "/html/body/app-root/ion-app/div/div/div[2]/div["
#                                        "2]/div/ion-router-outlet/app-page-list-songs/ion-content/div/div/div["
#                                        "2]/div/div[2]/app-song-list/div/div/button")
# button.click()
#
# # wait for the page to load
# # element = WebDriverWait(driver, 10).until(
# #     EC.invisibility_of_element_located(By.CSS_SELECTOR, "div button")
# # )
# # store it to string variable
#
#
# # page_source = driver.page_source
#
# soup = BeautifulSoup(html, "lxml")
#
# all_songs = soup.find_all(name="h5", class_="text-white m-0 text-truncate")
# print(all_songs)
# songs = [songs.get_text().strip("\n\t") for songs in all_songs]
import requests

url = "https://www.praisecharts.com/api/elastic/song-list/top-100-contemporary-hymns-of-2020"

querystring = {"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJNZW1iZXJJRCI6MTIzNDgyOCwic3ViIjoxMjM0ODI4LCJpc3MiOiJo"
                        "dHRwczovL3d3dy5wcmFpc2VjaGFydHMuY29tL3BjNS9hdXRoZW50aWNhdGUiLCJpYXQiOjE2NzA2NzE3NTgsImV4cCI6MT"
                        "Y3MzI2Mzc1OCwibmJmIjoxNjcwNjcxNzU4LCJqdGkiOiJMR0VPdlc2WWNGYVJXR1lQIn0._YGZ3Ea_WNKDi9ujMxzE1Q"
                        "FkgBxePxnQ5c4ee3QEHdg", "libraryId": "319623"}

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

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

data = response.json()

for song in data["songs"]:
    print(song["details"]["catalog_item_title"])
