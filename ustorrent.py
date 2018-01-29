from urllib import request
from bs4 import BeautifulSoup
import re
import csv
import time


class USAV():

    def __init__(self, page=0):
        self.HEADERS ={'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
        self.page = page

    def get_torrent_urls(self, page):
        torrent_urls = {}
        for i in range(page+1):
            url = r'http://www.btsone.cc/cat/id/8/page/%s/' % i
            response = request.urlopen(request.Request(url,headers=self.HEADERS))
            soup = BeautifulSoup(response, 'lxml')
            for link in soup.find_all(class_='tname'):
                torrent_urls[link.a.string] = r'https://www.bt-scene.cc'+link.a.get('href')
        return torrent_urls

    def get_magnets(self):
        magnet_dict = {}
        torrent_urls = self.get_torrent_urls(self.page)
        for name, url in torrent_urls.items():
            html = request.urlopen(request.Request(url, headers=self.HEADERS)).read().decode('utf-8')
            pattern = re.compile("magnet.*(?=\">)")
            match = pattern.search(html).group()
            time.sleep(1)
            magnet_dict[name] = match
            print(magnet_dict[name])
        return magnet_dict

if __name__ == '__main__':
    crawler = USAV()
    magnet_list = crawler.get_magnets()
    with open('outputs/us_magnet_list.csv','w',newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for key,value in magnet_list.items():
            writer.writerow([key,value])
        csvfile.close()


