import bs4
import re
import pandas as pd
import requests

def parse_list(url: str, parse_type: str) -> pd.DataFrame:
    """
    Scrape and parse song or album data from a given URL.
    
    Parameters:
        url (str): The URL to scrape.
        parse_type (str): The type of data to parse ("song" or "album").
        
    Returns:
        pd.DataFrame: A DataFrame containing the scraped Artist, Title, and Year information.
    """
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to get URL: {e}")
        return pd.DataFrame()

    soup = bs4.BeautifulSoup(r.content.decode("utf-8", "ignore"), "lxml")
    song_strings = [str(x).strip("<h2>").strip("</") for x in soup.find_all("h2")]

    # Decide the regex pattern based on parse_type
    title_pattern = r'“(.*?)”' if parse_type == "song" else r"<em>(.*?)</em>"

    artists, titles, years = [], [], []
    for s in song_strings:
        artists.append(s.split(":")[0])
        title_match = re.findall(title_pattern, s)
        titles.append(title_match[0] if title_match else "Unknown")
        year_match = re.findall(r"\(([0-9]{4})\)", s)
        years.append(year_match[0] if year_match else "Unknown")

    df = pd.DataFrame({"Artist": artists, "Title": titles, "Year": years})
    return df
