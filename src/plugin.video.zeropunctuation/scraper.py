import urllib, urllib2, re

URL = 'http://www.escapistmagazine.com/videos/view/zero-punctuation'

def scrape():
	data=[]

	req = urllib2.Request(URL)
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
        response = urllib2.urlopen(req)
        link=response.read()
        response.close()

	main_content = re.compile("<div id=\'gallery_display\'>(.*?)<div id=\'recent_site\'", re.MULTILINE).findall(link)[0]
	pattern="<div class=\'filmstrip_video\'><a href=\'(.*?)\'><img src=\'(.*?)\'></a><div class=\'title\'><i>(.*?)</i></div><div class=\'date\'>Date: (..)/(..)/(....)</div>"
        match=re.compile(pattern, re.MULTILINE).findall(main_content)
        for url,img,name,month,day,year in match:
		data.append((name,url,img,"%s-%s-%s"%(year,month,day)))
	return data

print scrape()
