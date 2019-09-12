import requests
from bs4 import BeautifulSoup
import sys
from lxml import etree
def get_url_content(url:str):
    """
        url:需要解析的url
        return：selector对象
    """
    rst=None
    r=requests.get(url)
    if r.status_code!=200:
        print('网页无法打开')
    r.encoding='utf-8'
    html=r.text
    try:
        selector = etree.HTML(html)
        return selector
    except Exception as identifier:
        print(identifier)
        return None
def get_url_sessions(chaptersUrl):

    """
        chaptersUrl:章的链接，如创世纪第一章链接
        return：这章的所有小节内容
    """
    rst=[]
    for chapters,url in enumerate(chaptersUrl):
        try:
            selector =get_url_content(url)
            title=selector.xpath('//span[@class="info"]/text()')    
        except Exception as identifier:
            print(f'chapters:{chapters}',identifier)
            continue
        # title=list(map(lambda t: str(chapters+1)+':'+str(t[0]+1)+' '+t[1].strip()+'\n',enumerate(title)))
        content=list(map(lambda t: t[1].strip()+'\n',enumerate(title)))
        session_index=list(map(lambda t: t[0]+1,enumerate(title)))
        rst+=(list(zip([chapters+1]*len(session_index),session_index,content)))
    if rst==[]:
        return []
    else:
        return rst
def get_url_shu(mainUrl):
    """
        mainUrl:网址主链接
        return：经文列表,及名称的迭代器
    """
    from itertools import chain
    selector=get_url_content(mainUrl)
    if selector is None:
        return []
    shus=selector.xpath('//ul[@class="biblelist"]')

    if len(shus)==0:
        return []
    shusUrl=[]
    shusName=[]
    for item in shus:
        shusUrl.extend(map(lambda x:x.xpath('.//a/@href')[0],item))
        shusName.extend(map(lambda x:x.xpath('.//a/text()')[0],item))
    # shusUrl=(list(shusUrl))
    # shusName=(list(shusName))
    rst=dict(zip(shusName,shusUrl))   
    return rst
    
def get_url_chapters(node_path:str):
    """
        node_path:哪篇经文链接，如创世纪
        return：这篇经文所有章节网址
    """
    rst={}
    selector=get_url_content(node_path)
    if selector is None:
        return rst
    chapters=selector.xpath('//div[@class="pageBox"]')    
    if len(chapters)==0:
        return rst    
    chapters_index=chapters[0].xpath('.//*/text()')
    chapters=list(map(lambda x: x.strip(),chapters_index))
    chapters=list(map(lambda x: node_path.split('.html')[0]+'_'+x+'.html',chapters))
    if len(chapters)==0: return rst
    rst=dict(zip(chapters_index,chapters))
    # rst=chapters
    return rst
mainUrl='http://bible.fqjdt.com/nuv/1.html'
chaptersUrl=get_url_shu(mainUrl)
# print(chaptersUrl)
datas=[]
from itertools import chain
for shuName,shusUrl in chaptersUrl.items():
    # for chapterIndex,chapterUrl in get_url_chapters(shusUrl).items():
    for chapter,session,content in get_url_sessions(get_url_chapters(shusUrl).values()):
        data=f'{shuName} {chapter}:{session} {content}'
        datas.append(data)
with open('1.txt','w+',encoding='utf-8') as f:
    f.writelines([item+'\n' for item in datas])

