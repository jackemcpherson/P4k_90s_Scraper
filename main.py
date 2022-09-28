url = "https://pitchfork.com/features/lists-and-guides/the-best-songs-of-the-1990s/"


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


df = parseSongList(url).to_csv(
    "P4K_Top_250_Songs_1990s.csv", index=False, encoding="utf-8-sig"
)
