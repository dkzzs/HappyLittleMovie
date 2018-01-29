from urllib import request
import datetime
import re
import os.path

def callback(a,b,c):
    '''
    :param a:chunck
    :param b:size
    :param c:filesize
    :return:
    '''
    print('%.2f%%'%(100*a*b/c))

def save_file(url, filename):
    t = datetime.datetime.now()
    print(t)
    if os.path.isfile(filename):
        filesize = os.path.getsize(filename)/1024/1024
        print(filename, "already exists, %sMB" % filesize)
        return
    else:
        print("Downloading")
        # r = requests.get(url, stream=True)
        r = request.urlretrieve(url, filename, callback)
        # with open(filename,'wb') as f:
        #     f.write(r)
        print(datetime.datetime.now() - t)
        print(filename, "downloaded")

def download_url(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
    content = request.urlopen(request.Request(url, headers=header)).read().decode('gbk')
    pattern = re.compile(r"http://m4.26ts.com/[.0-9-a-zA-Z]*.mp4")
    match = pattern.search(content)

    if match:
        movie_url = match.group()
        save_file(movie_url, movie_url[19:])
    else:
        print("Nothing")

# urls = ["http://www.46ek.com/view/22133.html",]
# count = 0
# for url in urls:
#     count+=1
#     print("Downloading... ", count)
#     download_url(url)
# print("Done")

xxx = r'http://big.downcc.com/bigfile/100/hsjj2ghgzhwmb_downcc.com.rar'
save_file(xxx,'HJ.exe')