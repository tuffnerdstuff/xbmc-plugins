import urllib,urllib2,re,xbmcplugin,xbmcgui,scraper

URL= 'http://www.escapistmagazine.com/videos/view/zero-punctuation'
                       
def buildVideoIndex(url):
        data=scraper.scrape(url)
	nextLinkUrl=scraper.scrapeNextPageLink()
        for name,info_url,img,date in data:
                addLink(name,info_url,3,img)
	if (nextLinkUrl != None):
		addDir("[Next Page >>]",nextLinkUrl,2,'')
        
def resolveVideoLink(url):
	video_url=scraper.scrapeVideoLink(url)
	listitem = xbmcgui.ListItem(path=video_url)
	print "[RESOLVEURL]" + video_url
	return xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, listitem)

                
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param




def addLink(name,url,mode,iconimage):
	u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)     
	ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
	# This property must be set or otherwise there will be no handle set when the video is selected
	# and setResolvedUrl will fail (invalid handle!)
	liz.setProperty('IsPlayable', 'true')
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok


def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
        
              
params=get_params()
url=None
name=None
mode=None

try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)

if mode==None or url==None or len(url)<1:
        print "[INDEX]"
        buildVideoIndex(URL)

if mode==2:
	print "[INDEX] url: " + url
	buildVideoIndex(url)
        
# After the video has been selected, the actual video url is resolved
elif mode==3:
	print "[RESOLVEURL] "+url
	resolveVideoLink(url)


if mode < 3: xbmcplugin.endOfDirectory(int(sys.argv[1]))
