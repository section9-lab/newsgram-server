from fastapi import FastAPI
from datetime import datetime
import whois

app = FastAPI()

@app.get("/")
async def root():
    res = {
        "time": datetime.now(),
        "des": "this is home page"
    }
    return res

@app.get("/url/{item_url}")
async def get_url(item_url):
    if item_url == None:
        item_url = "www.baidu.com"
    res = {
        "time": datetime.now(),
        "url": item_url,
        "whois": whois.whois(item_url)
    }
    return res
