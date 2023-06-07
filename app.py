from flask import Flask
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import tldextract
import whois
import requests
import sys

app = Flask(__name__)


@app.route("/", methods=['GET'])
def root():
    res = {
        'Time': datetime.now(),
        'About': 'this is home page',
        'Help': 'Please try   https://dns-insight-service.onrender.com/url/www.example.com'
    }
    return res


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
        html = conn.get(url, stream=True, headers=headers, timeout=10)
        soup = BeautifulSoup(html.content, 'html.parser')
        job_bt = soup.findAll('h2')
        for i in job_bt:
            link = i.a.get('href')
            suffix=tldextract.extract(link).suffix
            domain = tldextract.extract(link).domain
            subdomain = tldextract.extract(link).subdomain
            if subdomain is None:
                domains = str(urlparse(link).scheme + "://" + domain + "." + suffix)
            else:
                domains = str(urlparse(link).scheme + "://" + subdomain+"."+domain+"."+suffix)
            if domains is None:
                pass
            if domains in Subdomain:
                pass
            else:
                Subdomain.append(domains)
                print(domains)
    return Subdomain
