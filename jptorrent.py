from urllib import request
from bs4 import BeautifulSoup
import re
import csv
import time


class JPAV():

    def __init__(self):
        self.HEADERS ={'User-Agent': 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)'}

    def get_magnets(self,codes):
        magnet_dict = {}
        for code in codes:
            time.sleep(1)
            html = request.urlopen(request.Request(r'https://www.zhongziso.com/list_click/%s/1' % code, headers=self.HEADERS)).read().decode('utf-8')
            # back up url
            # content = request.urlopen(request.Request(r'http://www.sobt8.com/q/%s.html'%code, headers=self.HEADERS)).read().decode('utf-8')
            pattern = re.compile('class="ls-magnet"><a href="(magnet.*?)">')
            magnets = re.findall(pattern, html)
            if magnets:
                print('Find Torrent for %s' % code)
                magnet_dict[code] = magnets[0]
                # print(magnets[0])
            else:
                print('Can not Find Torrent for %s' % code)
        return magnet_dict

if __name__ == '__main__':
    crawler = JPAV()
    inputs = input("Enter codes below (separated by comma): \n")
    codes = [code.strip() for code in inputs.split(',')]
    print('Getting You Happy Movie for: ', codes)
    magnet_dict = crawler.get_magnets(codes)
    with open('outputs/jp_magnet_list.csv','w',newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for key,value in magnet_dict.items():
            writer.writerow([key,value])
        csvfile.close()
    input("Done! Enjoy!!!")




