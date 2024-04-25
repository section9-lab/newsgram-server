from flask import Flask
from flask import render_template
from flask_cors import CORS
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import tldextract
import whois
import requests
import json


app = Flask(__name__, static_folder='./dist', template_folder='./dist', static_url_path='')
CORS(app)

@app.route("/", methods=['GET'])
def root():
    return render_template('index.html', name='index')

"""
curl --location --request POST 'https://api.coze.com/open_api/v2/chat' 
--header 'Authorization: Bearer pat_rElexXLd5jhNOwpJ7T9R5ELpzWiDZ420hCJwpgXYYRjSm5rAoz0QtDgHV5QdMqK5' 
--header 'Content-Type: application/json' 
--header 'Accept: */*' 
--header 'Host: api.coze.com' 
--header 'Connection: keep-alive' 
--data-raw '{
    "conversation_id": "123",
    "bot_id": "7360968597655257096",
    "user": "29032201862555",
    "query": "run",
    "stream": false
}'
"""
@app.route("/news", methods=['GET'])
def coze():
    """
    coze api
    """
    '''
    url="https://api.coze.com/open_api/v2/chat"
    headers={
        'Authorization': 'Bearer pat_rElexXLd5jhNOwpJ7T9R5ELpzWiDZ420hCJwpgXYYRjSm5rAoz0QtDgHV5QdMqK5',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Host': 'api.coze.com',
        'Connection': 'keep-alive' 
    }
    data_json = {
            "stream": False,
            "conversation_id": "123",
            "bot_id": "7360968597655257096",
            "user": "29032201862555",
            "query": "run"
        }
    response = requests.post(url=url,headers=headers,data=json.dumps(data_json))
    response.text
    '''
    data = [
        {
            "title": "新闻标题1",
            "content": "新闻内容谢谢谢谢谢谢谢谢谢谢谢谢谢谢谢谢1",
        },
        {
            "title": "新闻标题2",
            "content": "新闻内容谢谢谢谢谢谢谢谢谢谢谢谢谢谢谢谢1",
        },
                {
            "title": "新闻标题3",
            "content": "新闻内容谢谢谢谢谢谢谢谢谢谢谢谢谢谢谢谢1",
        },
                {
            "title": "新闻标题4",
            "content": "新闻内容谢谢谢谢谢谢谢谢谢谢谢谢谢谢谢谢1",
        },
    ]
    return json.dumps(data)



@app.route("/hacker", methods=['GET'])
def hackerNews():
    data = []
    ''' 请求HackerNews '''
    url="https://news.ycombinator.com/news"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url=url,headers=headers)
    html = response.text
    
    bs = BeautifulSoup(html,'html.parser')
    data.append(bs.body)

    return json.dumps(data)




@app.route("/whois/<domain>", methods=['GET'])
def whois(domain):
    if domain is None:
        return "input is null"
    res = {
        "whois": whois.whois(domain),
    }
    return res


@app.route("/sub_url/<site>", methods=['GET'])
def sub_url(site, pages=10):
    if site is None:
        return "input is null"
    Subdomain = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',
        'Accept': '*/*',
        'Accept-Language': 'en-us,en;q=0.5',
        'Accept-Encoding': 'qzip,deflate',
        'referer': 'http://cn.bing.com/search?q=email+site%3abaidu.com&qs=n&sp=-1&pq=emailsie%3abaidu.com&first=2&FORM=PERE1'
    }

    for i in range(1, int(pages) + 1):
        url = "https://cn.bing.com/search?q=site%3a" + site + "&qs=n&form=QBRE&go=Search&qs=ds&first=" + str(
            (int(i) - 1) * 10) + "&FORM=PERE"
        conn = requests.session()
        conn.get('http://cn.bing.com', headers=headers)
        html = conn.get(url, stream=True, headers=headers, timeout=5)
        soup = BeautifulSoup(html.content, 'html.parser')
        job_bt = soup.findAll('h2')
        for i in job_bt:
            link = i.a.get('href')
            suffix = tldextract.extract(link).suffix
            domain = tldextract.extract(link).domain
            subdomain = tldextract.extract(link).subdomain
            if subdomain is None:
                domains = str(urlparse(link).scheme + "://" + domain + "." + suffix)
            else:
                domains = str(urlparse(link).scheme + "://" + subdomain + "." + domain + "." + suffix)
            if domains is None:
                pass
            if domains in Subdomain:
                pass
            else:
                Subdomain.append(domains)
                print(domains)
    return Subdomain
