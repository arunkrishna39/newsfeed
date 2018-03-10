import json
from lxml import html
from lxml.html import parse
from lxml.cssselect import CSSSelector
from bottle import route
@route('/')
def hello():
    return "Hello World!"
@route('/news', method='GET')
def news_show():
    
    return json.dumps(get_latest_from_manorama())
def get_latest_from_manorama():
    doc = parse('http://www.manoramaonline.com/').getroot()
    newslist = list()
    for link in doc.cssselect('article.latest_news_main_thumb_list'):
     newslist.append({'desc':link.cssselect('h2.Georgia01 a')[0].text_content().encode("utf-8"), 'url':'http://www.manoramaonline.com'+link.cssselect('h2.Georgia01 a')[0].get("href"), 'image':link.cssselect('div.stories_slot_img a img')[0].get("src")})
    return newslist   
    