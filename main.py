import re

import bs4
import pandas as pd
import requests

songs_url = (
    "https://pitchfork.com/features/lists-and-guides/the-best-songs-of-the-1990s/"
)
album_url = (
    "https://pitchfork.com/features/lists-and-guides/the-best-albums-of-the-1990s/"
)


def parseSongList(url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content.decode("utf-8", "ignore"), "lxml")
    song_strings = [str(x).strip("<h2>").strip("</") for x in soup.find_all("h2")]
    artists = [x.split(":")[0] for x in song_strings]
    titles = [re.findall("“(.*?)”", x)[0] for x in song_strings]
    years = [re.findall(r"\(([0-9]{4}?)\)", x)[0] for x in song_strings]
    scraped_values = {"Artist": artists, "Title": titles, "Year": years}
    df = pd.DataFrame.from_dict(scraped_values)
    return df


def parseAlbumList(url):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content.decode("utf-8", "ignore"), "lxml")
    song_strings = [str(x).strip("<h2>").strip("</") for x in soup.find_all("h2")]
    artists = [x.split(":")[0] for x in song_strings]
    titles = [re.findall(r"<em>(.*?)</em>", x)[0] for x in song_strings]
    years = [re.findall(r"\(([0-9]{4}?)\)", x)[0] for x in song_strings]
    scraped_values = {"Artist": artists, "Title": titles, "Year": years}
    df = pd.DataFrame.from_dict(scraped_values)
    return df


df = parseSongList(songs_url).to_csv(
    "P4K_Top_250_Songs_1990s.csv", index=False, encoding="utf-8-sig"
)

df2 = parseAlbumList(album_url).to_csv(
    "P4K_Top_250_Albums_1990s.csv", index=False, encoding="utf-8-sig"
)
