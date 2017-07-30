

#coding = utf-8
from Crypto.Cipher import AES
import base64
import requests
import json,sys,io

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')



def get_params(first_param,forth_param):
    iv = "0102030405060708"
    first_key = forth_param
    second_key = 16 * 'F'
    h_encText = AES_encrypt(first_param, first_key, iv)
    h_encText = AES_encrypt(h_encText, second_key, iv)
    return h_encText


def get_encSecKey():
    encSecKey = "257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c"
    return encSecKey
    

def AES_encrypt(text, secKey,iv):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(secKey, 2, iv)
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext.decode()


def get_json(url,headers,params, encSecKey):
    data = {
         "params": params,
         "encSecKey": encSecKey
    }
    response = requests.post(url, headers=headers, data=data)
    return response.content

def get_playlist(uid):
    
    headers = {
    'Cookie': 'appver=1.5.0.75771;',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Referer': 'http://music.163.com/'
    }

    first_param = "{uid:\""+str(uid)+"\", offset:\"0\", total:\"true\", limit:\"20\", csrf_token:\"\"}"
    second_param = "010001"
    third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
    forth_param = "0CoJUm6Qyw8W8jud"

    url = "http://music.163.com/weapi/user/playlist?csrf_token="
    params = get_params(first_param,forth_param);
    encSecKey = get_encSecKey();
    json_text = get_json(url,headers, params, encSecKey)
    json_dict = json.loads(json_text.decode('utf-8'))
    print("已下是他/她的歌单：")
    play_list={}
    for item in json_dict['playlist']:
        print(item['name'],'-ID:',item['id'])
        play_list[item['name']]=item['id']
    return play_list

def get_comments(songid,page):
    # offset的取值为:(评论页数-1)*20,total第一页为true，其余页为false
    url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_"+str(songid)+"/?csrf_token="

    headers = {
    'Cookie': 'appver=1.5.0.75771;',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    'Referer': 'http://music.163.com/'
    }

    if page==1:
        first_param = "{rid:\"\", offset:\"0\", total:\"true\", limit:\"20\", csrf_token:\"\"}"
    else:
        first_param = '{rid:"", offset:"%s", total:"%s", limit:"20", csrf_token:""}' %(str((page-1)*20),'false')
    #二三四参数固定
    second_param = "010001"
    third_param = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
    forth_param = "0CoJUm6Qyw8W8jud"

    
    params = get_params(first_param,forth_param);
    encSecKey = get_encSecKey();
    json_text = get_json(url,headers, params, encSecKey)
    json_dict = json.loads(json_text.decode('utf-8'))
    #print(json_dict['comments'])
    comments_list=[]
    for comments in json_dict['comments']:
        #print(comments)
        comments_list.append((comments['user']['nickname'],comments['content'],str(page)))
    with open('comments.txt','at',encoding= 'utf8') as f1:
        with open('hi_comments.txt','at',encoding= 'utf8') as f2:
            for comment in comments_list: 
                if comment[0]!='恰恰恰好的':
                    f1.write('<:>'.join(comment))
                    f1.write('\n')
                else:
                    f2.write('<:>'.join(comment))
                    f2.write('\n')

    return json_dict['total'],comments_list

def get_all_comments(songid):
    total_comments,_=get_comments(songid,1)
    all_comments=[]
    if(total_comments % 20 == 0):
        page = total_comments // 20
    else:
        page = total_comments // 20 + 1 
    for i in range(1,page+1):
        _,comments_list=get_comments(songid,i)
        all_comments.extend(comments_list)
    return all_comments
    #print(total_comments)
#get_playlist(85786265)
# x=get_all_comments(273288)
# print(x)
# for y in x:
#     if y[0]=='恰恰恰好的':
#         print(y[1])

        