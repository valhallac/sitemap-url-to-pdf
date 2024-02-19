import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def extract_urls_from_sitemap(url_sitemap):
    sitemap = []
    urls = []
    sitemap_crawled = []
    xml = requests.get(url_sitemap)
    xml_parsed = BeautifulSoup(xml.content, "xml")
    if xml_parsed.find_all("sitemap"):
        sitemaps = xml_parsed.find_all("loc")
        for s in sitemaps:
            sitemap.append(s.text)
        for s in sitemap:
            uis = requests.get(s)
            uis_parsed = BeautifulSoup(uis.content, "xml")
            urls_loc1 = uis_parsed.find_all("loc")
            for u in urls_loc1:
                urls.append(u.text)
                sitemap_crawled.append(s)
    else:
        url = xml_parsed.find_all("loc")
        for u in url:
            urls.append(u.text)
            sitemap_crawled.append(url_sitemap)
    return urls, sitemap_crawled

urls,sitemap_crawled = extract_urls_from_sitemap("https://docs.mulesoft.com/sitemap.xml")

df = pd.DataFrame({
    "urls":urls
})
df.to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)),"urls-sitemap.csv"), encoding="utf-8", index=False)