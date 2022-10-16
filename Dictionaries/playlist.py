playlist = {
    'title': 'vicious',
    'author': 'colt steele',
    'songs': [
        {'title' : 'song1' , 'artist' : ['blue'] , 'duration' : 2.5},
        {'title' : 'song2' , 'artist' : ['sky'] , 'duration' : 2.0}
        
    ]
}

for song in playlist['songs']:
    print(song['title'])