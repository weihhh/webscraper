import get_search,get_songlist

all_songs_id=[]
play_list=get_songlist.get_playlist(get_search.get_uid('IImagination'))
for playlistid in play_list:
    #print(get_search.get_songid(playlistid))
    all_songs_id.extend(get_search.get_songid(playlistid))

#print(all_songs_id)