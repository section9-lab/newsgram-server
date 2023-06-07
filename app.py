from flask import Flask
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import whois
import requests
import sys

app = Flask(__name__)


@app.route("/", methods=['GET'])
def root():
    res = {
        'time': datetime.now(),
        'des': 'this is home page'
               'help' 'try: https://dns-insight-service.onrender.com/url/www.example.com'
    }
    return res


@app.route("/sub_domain/bing/<domain>", methods=['GET'])
def sub_domain(domain, page=100):
    if domain is None:
        return "input is null"
    Subdomain_list = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0'}
    for i in range(int(page)):
        try:
            url = "https://cn.bing.com/search?q=site%3A" + domain + "&qs=n&form=QBRE&sp=-1&pq=site%3A" + domain + "&sc=2-11&sk=&cvid=C1A7FC61462345B1A71F431E60467C43&toHttps=1&redig=3FEC4F2BE86247E8AE3BB965A62CD454&pn=2&first=1&FROM=PERE"  # .format(i)
            response = requests.get(url, headers=headers, timeout=3)
        except:
            pass
        soup = BeautifulSoup(response.content, 'html.parser')
        job_bt = soup.findAll('h2')
        for in_bt in job_bt:
            link = in_bt.a.get('href')
            domain = str(urlparse(link).scheme + "://" + urlparse(link).netloc)
            Subdomain_list.append(domain)
    Subdomain_list = list(set(Subdomain_list))  # 去重
    print(Subdomain_list)

    res = {
        "whois": whois.whois(domain),
        "data": Subdomain_list
    }
    return res
