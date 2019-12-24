import json
import re
import requests


headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-US,en;q=0.8',
        'Cache-Control': 'max-age=0',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
        'Connection': 'keep-alive',
        'Referer': 'http://www.baidu.com/'
    }
def dianshiju():
    url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E5%9B%BD%E4%BA%A7%E5%89%A7&sort=recommend&page_limit=20&page_start=0"
    response = requests.get(url, headers=headers)
    response_json = json.loads(response.text)
    for list in response_json['subjects']:
        print(list['title'], list['rate'], list['cover'], list['url'])
        detail(list['id'])


def detail(id):
    url = 'https://m.douban.com/rexxar/api/v2/tv/'+id
    response = requests.get(url, headers=headers)
    response_json = json.loads(response.text)
    #r1 = re.findall('<div id="info">.*?</div>', response.text, re.S)[0]

    #print(r1)
    print(response_json['card_subtitle'])
    print(response_json['actors'])
    print(response_json['genres'])
    print(response_json['durations'][0])
    print(response_json['intro'])


if __name__ == '__main__':
    dianshiju()