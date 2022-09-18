from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

ndtv_links = []
ndtv_descriptions = []
ndtv_images = []
ndtv_titles = []


my_url = "https://www.ndtv.com/world-news"
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", {"class": "news_Itm"})
for container in containers:
    images = container.findAll("div", {"class": "news_Itm-img"})
    for image in images:
        ndtv_images.append(image.a.img["src"])

    details = container.findAll("div", {"class": "news_Itm-cont"})
    for detail in details:
        ndtv_titles.append(detail.h2.text)
        ndtv_links.append(detail.h2.a["href"])
        ndtv_descriptions.append(detail.p.get_text())