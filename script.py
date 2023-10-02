from main import parse_list  # Import the refactored function from main.py

# URLs to scrape for song and album information
songs_url = "https://pitchfork.com/features/lists-and-guides/the-best-songs-of-the-1990s/"
album_url = "https://pitchfork.com/features/lists-and-guides/the-best-albums-of-the-1990s/"

# Main execution
if __name__ == "__main__":
    # Scrape and save song information
    parse_list(songs_url, "song").to_csv(
        "P4K_Top_250_Songs_1990s.csv", index=False, encoding="utf-8-sig"
    )
    
    # Scrape and save album information
    parse_list(album_url, "album").to_csv(
        "P4K_Top_150_Albums_1990s.csv", index=False, encoding="utf-8-sig"
    )
