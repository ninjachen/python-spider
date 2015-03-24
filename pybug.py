#coding:utf-8
import urllib2
import re
import urllib
import os
 
url_list = [
	'http://www.douban.com/photos/album/32276368/?start=%d', 
	'http://www.douban.com/photos/album/59507212/?start=%d'
]
 
page_list = [8, 8]
 
folder_list = [u'建筑', u'文字']
 
re_pic = re.compile(r'<div class="photo_wrap">.+?<img src="(.+?)" />', re.DOTALL) 
 
# fake webbrower
headers = {
	'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/39.0.2171.65 Chrome/39.0.2171.65 Safari/537.36'
}
 
 
 
 
# main py
for i, j, g in zip(url_list, page_list, folder_list):
	if not os.path.exists(g):
		os.mkdir(g)
	os.chdir(g)
	for k in range(0, j):
		url = i % (k*18)
		opener = urllib2.build_opener()
		opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/39.0.2171.65 Chrome/39.0.2171.65 Safari/537.36')]
		html = opener.open(url).read()
		pics = re_pic.findall(html)
		for h in pics:
			if 'thumb' in h:
				h = h.replace('thumb', 'photo')
			pic_name = h[47:]
			if not os.path.isfile(pic_name):
				urllib.urlretrieve(h, pic_name)
				print 'Download  ' + pic_name + '  succeed!'
		print 'folder: ', g , '  page: ', k, '/', j, 'Done!'
	os.chdir("..")
