import pickle
import os
import get_search,get_songlist

#给出需要寻找的用户名
username='恰恰恰好的'

all_songs_id={}#存放需要搜寻的用户歌曲id


if not os.path.exists('./tmp'):
    print('creat tmp dir!')
    os.mkdir('./tmp')
    
if os.path.exists('./tmp/{}.pkl'.format(username)):
    #获取pickle好的歌曲数据
    print('load cache data!')
    pkl=open(username+'.pkl','rb')
    all_songs_id=pickle.load(pkl)
    pkl.close()
else:
    userid,userdict=get_search.get_uid(username)#获得用户id和包含所有信息的dict

    play_list=get_songlist.get_playlist(userid)#获得用户所有歌单id的字典:歌单名：id

    for playlistname in play_list:
        #print(get_search.get_songid(playlistid))
        all_songs_id[playlistname]=get_search.get_songid(play_list[playlistname])

    output=open('./tmp/{}.pkl'.format(username),'wb')
    pickle.dump(all_songs_id,output)
    output.close()

for song in all_songs_id['opera_for_uncle']:
    print(song[1])
    x=get_songlist.get_all_comments(song[1])