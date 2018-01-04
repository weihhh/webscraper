import requests,json,sys,io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

def get_rank():
    headers = {
        'Cookie': 'appver=1.5.0.75771;',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
        'Referer': 'http://music.163.com/'
    }

    url = "http://music.163.com/user/songs/rank?id=72937621"
    response = requests.get(url, headers=headers)
    print(response.text)

    return response#返回的是包含歌名，id对的列表
 
print(get_rank())