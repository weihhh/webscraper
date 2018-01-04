import pickle
import get_search,get_songlist

#给出需要寻找的用户名
username='此昵称已被抢也被抢了'
all_songs_id={}#存放需要搜寻的用户歌曲id

#已下经过第一次获取歌曲id后就可以不运行
'''
userid,userdict=get_search.get_uid(username)#获得用户id和包含所有信息的dict

play_list=get_songlist.get_playlist(userid)#获得用户所有歌单id的字典:歌单名：id

for playlistname in play_list:
    #print(get_search.get_songid(playlistid))
    all_songs_id[playlistname]=get_search.get_songid(play_list[playlistname])

output=open(username+'.pkl','wb')
pickle.dump(all_songs_id,output)
output.close()
'''
#获取pickle好的歌曲数据
pkl=open(username+'.pkl','rb')
all_songs_id=pickle.load(pkl)
pkl.close()

for item in [all_songs_id['OST'],all_songs_id['؏؏ᖗ¤̴̶̷̤́‧̫̮¤̴̶̷̤̀)ᖘ؏؏']]:
    for song in item:
        print('进行---> ',song[0])
        get_songlist.get_all_comments(song[0],song[1],username)
