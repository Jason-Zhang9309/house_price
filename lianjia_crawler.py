#coding=UTF-8
from urllib.error import URLError
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pymysql
import ssl
import re

#from pymysql import Error

def decode_page(page_bytes, charsets=('utf-8',)):
    """通过指定的字符集对页面进行解码(不是每个网站都将字符集设置为utf-8)"""
    page_html = None
    for charset in charsets:
        try:
            page_html = page_bytes.decode(charset)
            break
        except UnicodeDecodeError:
            pass
            # logging.error('Decode:', error)
    return page_html


def get_page_html(seed_url, *, retry_times=3, charsets=('utf-8',)):
    """获取页面的HTML代码(通过递归实现指定次数的重试操作)"""
    page_html = None
    try:
        page_html = decode_page(urlopen(seed_url).read(), charsets)
    except URLError:
        # logging.error('URL:', error)
        if retry_times > 0:
            return get_page_html(seed_url, retry_times=retry_times - 1,
                                 charsets=charsets)
    return page_html

def data_wash(list):
        list[2] = str(list[2])[:-2]
        list[3] = str(list[3][2:-3])
        list[7] = list[7].replace('.','-')
        return(list)

def to_mysql(data_list):

    data_list = data_wash(data_list)
    
    conn = pymysql.connect(host='localhost', port=3306,
                           database='house_price', user='root',
                           password='123456', charset='utf8')
    try:
        with conn.cursor() as cursor:
            result = cursor.execute(
                                    'insert into tb_sold_house values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)',data_list
                                    )

        if result == 1:
            print('添加成功！')

        conn.commit()
    except Exception as e:
        print(e,',入库异常，跳过该记录...')

    
    finally:
        conn.close()

"""

"""
def detail_crawl(link):

    detail_page_html = get_page_html(link, charsets=('utf-8', 'gbk', 'gb2312'))
    soup = BeautifulSoup(detail_page_html,'lxml')

    
    title_list = ['location','total_price','space','single_price','house_type','direction','open_date','sold_date','source_link','lianjia_number']
    

    
    data_list = ['','','','','','','','','','']
    divs = soup.find(class_ = 'wrapper')
    data_list[0] = divs.h1.string.split()[0]
    data_list[4] = divs.h1.string.split()[1]
    data_list[2] = divs.h1.string.split()[2]
    data_list[7] = divs.span.string.split()[0]
    data_list[8] = link
    data_list[9] = link.split('/')[-1].split('.')[0]

    divs_1 = soup.find(class_ = 'price')
    data_list[1] = divs_1.span.i.string

    divs_2 = soup.find(class_ = 'record_list')
    data_list[3] = divs_2.p.string.split(',')[0]
    

    divs2 = soup.find(class_ = 'base')
    
    for t in divs2.find_all('li'):
        if (str(t.get_text()))[0:4].rstrip()== '房屋朝向':
            data_list[5] = str(t.get_text())[4:].rstrip()

    divs3 = soup.find(class_ = 'transaction')
    
    for t in divs3.find_all('li'):
        if (str(t.get_text()))[0:4].rstrip()== '挂牌时间':
            data_list[6] = str(t.get_text())[4:].rstrip()

    data_dict = {}
    for i in range(len(data_list)):
        data_dict[title_list[i]] = data_list[i]
    print(data_dict)
    
    to_mysql(data_list)

def start_crawl(seed_url):
    """开始执行爬虫程序"""
   
    # 尝试用utf-8/gbk/gb2312三种字符集进行页面解码
    page_html = get_page_html(seed_url, charsets=('utf-8', 'gbk', 'gb2312'))
    
    soup = BeautifulSoup(page_html,'lxml')
    list_Content = soup.find(class_='listContent')
    lis = list_Content.find_all('li')
    links_list = []
    for t in lis:
        links_list.append(t.find(class_='img').attrs['href'])
    print(links_list)
    for link in links_list:
        detail_crawl(link)
    #detail_crawl(links_list)


def main():
    """主函数"""
    ssl._create_default_https_context = ssl._create_unverified_context
    start_crawl('https://bj.lianjia.com/chengjiao/pg2/')

if __name__ == '__main__':
    main()
