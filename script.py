from main import parseSongList, parseAlbumList

songs_url = (
    "https://pitchfork.com/features/lists-and-guides/the-best-songs-of-the-1990s/"
)
album_url = (
    "https://pitchfork.com/features/lists-and-guides/the-best-albums-of-the-1990s/"
)

if __name__ == "__main__":
    parseSongList(songs_url).to_csv(
        "P4K_Top_250_Songs_1990s.csv", index=False, encoding="utf-8-sig"
    )
    parseAlbumList(album_url).to_csv(
        "P4K_Top_150_Albums_1990s.csv", index=False, encoding="utf-8-sig"
    )
