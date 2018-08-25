# import spotipy

# spotify = spotipy.Spotify()
# name = 'Frank Ocean'
# results = spotify.search(q='artist:' + name, type='artist')
# print (results)


# import spotipy
# sp = spotipy.Spotify()

# results = sp.search(q='weezer', limit=20)
# for i, t in enumerate(results['tracks']['items']):
#     print (' ', i, t['name'])


import sys
import spotipy
import spotipy.util as util

# export SPOTIPY_CLIENT_ID ='c1ea3f3e70bb4c369149324035a5da3e'
# export SPOTIPY_CLIENT_SECRET='035f2e1af21740b7ac330e2c664051c2'
# export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'

# http://localhost:8888/callback
username = 'daxoneter@gmail.com'
# scope = 'user-library-read'
# scope = 'playlist-read-private'
# scope = 'user-library-modify'

# scope = 'user-read-recently-played'
scope = 'user-read-playback-state user-read-recently-played user-library-read playlist-read-private user-library-modify' 
if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print ("Usage: %s username" % (sys.argv[0],))
    sys.exit()

# util.prompt_for_user_token(username,scope,client_id='c1ea3f3e70bb4c369149324035a5da3e',client_secret='035f2e1af21740b7ac330e2c664051c2',redirect_uri='http://localhost:8888/callback')
token = util.prompt_for_user_token(username,scope,client_id='c1ea3f3e70bb4c369149324035a5da3e',client_secret='035f2e1af21740b7ac330e2c664051c2',redirect_uri='http://localhost:8888/callback')


# token = util.prompt_for_user_token(username, scope)


# if len(sys.argv) > 1:
#     name = ' '.join(sys.argv[1:])
# else:
#     name = 'Radiohead'
# if token: 
#     sp = spotipy.Spotify(auth=token)
#     results = sp.search(q='artist:' + name, type='artist')
#     items = results['artists']['items']
#     if len(items) > 0:
#         artist = items[0]
#         print (artist['name'], artist['images'][0]['url'])
# else: 
#     print('here')

uri = 'spotify:artist:1URnnhqYAYcrqrcwql10ft';
if token:
   
    sp = spotipy.Spotify(auth=token)
    artist = sp.artist(uri)
    # print('my call')
    # print(sp.current_user_saved_tracks())
    # print(artist['id'])
    albums = sp.artist_albums(artist['id'], album_type='album', country='US', limit=20, offset=0)
    # print(artist)
    # print(albums)

    print('-------Album Names--------')
    for item in albums['items']:
        name = item['name']
        print(name)
    
    print('--------Album Type---------')
    for item in albums['items']:
        albumType = item['album_type']
        print(albumType)

    print('-------Album URI-------') 
    for item in albums['items']:
        albumURI = item['uri']
        print(albumURI)
    
    print('--------Album Release Date--------')
    for item in albums['items']:
        releaseDate = item['release_date']
        print(releaseDate)

    print('----------Number of Tracks--------')
    for item in albums['items']:
        numTracks = item['total_tracks']
        print(numTracks)
    # results = sp.current_user_saved_tracks(limit=50)
    temp = sp.current_user_recently_played(limit=50)
    # print(temp)

    for item in temp['items']:
        timePlayed = item['played_at']
        songName = item['track']['name']
        print(songName + '   Time Played At   ' + timePlayed)

    currSong = sp.current_user_playing_track()
    print(currSong)
    # for item in temp['items']:
    #     itemName = item['track']['name']
    #     print(itemName)
    # x = sp.current_user_saved_albums(limit=20, offset=0)
    # song = sp.current_user_playing_track()
    # song = sp.current_user()
    # temp = sp.search('Nice For What', limit=1, offset=0, type='track', market=None)
    # print(temp)
    devices = sp.devices()
    # song = sp.current_user_saved_tracks_delete(tracks='1cTZMwcBJT0Ka3UJPXOeeN')
    print(devices)
    # print(song)
    # tempUser = sp.current_user_recently_played(limit=50)
    # print(temp)    
    # print(tempUser)
    # for item in results['items']:
    #     track = item['track']
    #     print (track['name'] + ' - ' + track['artists'][0]['name'])
else:
    print ("Can't get token for", username)

    