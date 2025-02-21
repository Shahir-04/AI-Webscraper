import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive",
    }
    web=requests.get(url,headers=headers).text
    return web

def extraxt_content(html_content):
    soup=BeautifulSoup(html_content,'html.parser')
    body_content=soup.body
    if body_content:
        return str(body_content)
    else:
        return ""

def clean_body_content(body_content):
    soup=BeautifulSoup(body_content,'html.parser')
    for i in soup(['script','style']):
        i.extract()

    clean_content=soup.get_text(separator='\n')
    clean_content='\n'.join(
        line.strip() for line in clean_content.splitlines() if line.strip()
    )
    return clean_content

def split_dom_content(dom_content,max_length=6000):
    return[
        dom_content[i:i+max_length] for i in range(0,len(dom_content),max_length)
    ]