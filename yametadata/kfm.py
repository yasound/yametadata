import xmltodict
import requests

KFM_BASE_COVER = 'http://www.k-fm.com/wp-content/plugins/4ways/_radio/pochettes/'
KFM_COVER_SIZE = 210

def find_metadata(cover_size=KFM_COVER_SIZE):
    url = 'http://static.k-fm.com/_radio/titrage.xml'
    params = {
    }
    try:
        r = requests.get(url, params=params)
    except:
        return None

    content = None
    try:
        content = r.content.decode("iso-8859-1").encode("UTF-8")
    except:
        content = None

    if content is None:
        try:
            content = r.content.encode('utf-8')
        except:
            content = r.content

    try:
        data = xmltodict.parse(content)
        current_radio = data['radio']['current']
        artist = current_radio.get('artist')
        name = current_radio.get('title')
        cover = current_radio.get('picture')
        if cover:
            cover = u'%s%s~%s' % (KFM_BASE_COVER, cover, cover_size)

        data = {
            'artist': artist,
            'name': name,
            'cover': cover
        }

    except:
        data = None

    return data
