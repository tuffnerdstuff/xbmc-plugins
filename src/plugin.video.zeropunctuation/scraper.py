import urllib, urllib2, re

URL = 'http://www.escapistmagazine.com/videos/view/zero-punctuation'
VIDEO_URL = 'http://www.escapistmagazine.com/videos/view/zero-punctuation/8298-Beyond-Two-Souls'

def readPage(url):
	req = urllib2.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        html=response.read()
        response.close()
	return html

def scrape(url):
	data=[]

	link = readPage(url)

	main_content = re.compile("<div id=\'gallery_display\'>(.*?)<div id=\'recent_site\'", re.MULTILINE).findall(link)[0]
	pattern="<div class=\'filmstrip_video\'><a href=\'(.*?)\'><img src=\'(.*?)\'></a><div class=\'title\'><i>(.*?)</i></div><div class=\'date\'>Date: (..)/(..)/(....)</div>"
        match=re.compile(pattern, re.MULTILINE).findall(main_content)
        for url,img,name,month,day,year in match:
		data.append((name,url,img,"%s-%s-%s"%(year,month,day)))
	return data

def scrapeVideoLink(url):
	html = readPage(url)
	pattern='<param name="flashvars" value="config=(.*?)"/>'
	match=re.compile(pattern, re.MULTILINE).findall(html)
	json_url=match[0]
	html_json = readPage(json_url)
	link_pattern = "\'url\':\'(.*?)\'"
	match=re.compile(link_pattern, re.MULTILINE).findall(html_json)
	return match[1]

print scrape(URL)
print scrapeVideoLink(VIDEO_URL)
