
def GetAlbumName(text: str) -> str:
    # Sample: 
    #   💽 Album: Mortal Kombat 1 (Original Video Game Soundtrack)
    album = text.split('\n')[0]
    # Get rid of "💽 Album: ..."
    album = album[8:].strip()
    # Get rid of "... (Original Game Soundtrack)"
    if '(' in album:
        album = album[:album.index('(')].strip()
    return album