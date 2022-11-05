import re

import bs4
import pandas as pd
import requests


def parseSongList(url: str):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content.decode("utf-8", "ignore"), "lxml")
    song_strings = [str(x).strip("<h2>").strip("</") for x in soup.find_all("h2")]
    artists = [x.split(":")[0] for x in song_strings]
    titles = [re.findall("“(.*?)”", x)[0] for x in song_strings]
    years = [re.findall(r"\(([0-9]{4}?)\)", x)[0] for x in song_strings]
    scraped_values = {"Artist": artists, "Title": titles, "Year": years}
    df = pd.DataFrame.from_dict(scraped_values)
    return df


def parseAlbumList(url: str):
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content.decode("utf-8", "ignore"), "lxml")
    song_strings = [str(x).strip("<h2>").strip("</") for x in soup.find_all("h2")]
    artists = [x.split(":")[0] for x in song_strings]
    titles = [re.findall(r"<em>(.*?)</em>", x)[0] for x in song_strings]
    years = [re.findall(r"\(([0-9]{4}?)\)", x)[0] for x in song_strings]
    scraped_values = {"Artist": artists, "Title": titles, "Year": years}
    df = pd.DataFrame.from_dict(scraped_values)
    return df
