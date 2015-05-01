#coding:utf-8
import requests,json,urllib2,urllib
from BeautifulSoup import BeautifulSoup

url = raw_input("Please enter URL:")
#url="http://item.jd.com/1217499.html"
pid=url.split('/')[-1].split('.')[0]
d={'User-Agent':'Mozilla/5.0'}
resp=requests.get(url,headers =d)
bs=BeautifulSoup(resp.content)


name=bs.find('div',{'id':'name'}).text
print 'Product Name:',name

print "======================================"

f = urllib2.urlopen('http://p.3.cn/prices/get?skuid=J_'+pid)
price=json.loads(f.read())
f.close()
print 'Product Price:',price[0]['p']

print "======================================"

a = r'http://club.jd.com/productpage/p-{}-s-0-t-3-p-0.html'.format(pid)
headers1 = {'GET': '',
            'Host': "club.jd.com",
            'User-Agent': "Mozilla/5.0 (Windows NT 6.2; rv:29.0) Gecko/20100101 Firefox/29.0",
            'Referer': 'http://item.jd.com/%s.html' % (pid)}

req = urllib2.Request(a, headers=headers1)
s = urllib2.urlopen(req)
dd = json.loads(s.read().decode('gbk', 'ignore'))
print 'Product commentCount£º',dd['productCommentSummary']['commentCount']

print "======================================"
for x in dd['hotCommentTagStatistics']:
    print 'Product TagS',x['name']


