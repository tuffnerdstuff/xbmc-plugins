import xbmcplugin
import xbmcgui

name = 'Zero Punctuation'
url = 'http://video.escapistmagazine.com/links/766d9ea2d7d02d7e2dec3a7c47146f9d/mp4/escapist/zero-punctuation/c18de1cf26b7b6078077180f3941a116.mp4'

def addDirectoryItem():
    li = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=pic)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)

def addPlayableItem():
    li = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage="")
    li.setInfo( type="Video", infoLabels={ "Title": name } )
    li.setProperty('IsPlayable', 'true')
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=False)

addPlayableItem()
