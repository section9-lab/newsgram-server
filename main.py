from fastapi import FastAPI
from datetime import datetime
import whois

app = FastAPI()

@app.get("/")
async def root():
    res = {
        "time": datetime.now(),
        "url": "www.baidu.com",
        "whois": whois.whois("www.baidu.com")
    }
    return res
