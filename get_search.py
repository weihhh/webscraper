import requests
import json,sys,io

def get_uid(username):    
    headers = {
        'Cookie': 'appver=1.5.0.75771;',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Referer': 'http://music.163.com/'
    }

    url = "http://music.163.com/api/search/pc"
    data = {
         "s": username,
         "offset": '0',
         'limit':'20',
         'type':'1002'
    }
    response = requests.post(url, headers=headers, data=data)
    jsondatadict=json.loads(response.text)#有resutl和code两个键
    resultdata=jsondatadict['result']['userprofiles']
    for item in resultdata:
        if item['nickname']==username:
            print('-成功找到:',item['nickname'],' -ID号为：',item['userId'],'-粉丝数：',item['followeds'])
            return item['userId'],item#返回用户id和包含用户所有信息的dict

#存在一次只能获得上限1000的歌曲，超过的解决办法还没有想到
def get_songid(playlistid):
    headers = {
        'Cookie': 'appver=1.5.0.75771;',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Referer': 'http://music.163.com/'
    }

    url = "http://music.163.com/api/playlist/detail?id="
    response = requests.get(url+str(playlistid), headers=headers)
    jsondatadict=json.loads(response.text)#result键->tracks键得到列表->name,id
    songidlist=[]
    for item in jsondatadict['result']['tracks']:
        #print('-歌名：',item['name'],'-ID',item['id'])
        songidlist.append((item['name'],item['id']))
    return songidlist#返回的是包含歌名，id对的列表
    #print(response.text)

#print(get_songid(139193755))
# print(type(get_uid('恰恰恰好的')))
