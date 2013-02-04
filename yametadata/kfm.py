import xmltodict
import requests

KFM_BASE_COVER = 'http://www.k-fm.com/wp-content/plugins/4ways/_radio/pochettes/'
KFM_COVER_SIZE_NORMAL = 68
KFM_COVER_SIZE_LARGE = 210


def find_metadata():
    """Return the current song.
    the returned data is a dict::

        dict = {
            'name': 'foo', # title
            'artist': 'bla' # artist name
            'cover': 'http://cover_normal', # url of normal cover
            'large_cover': 'http://cover_large' # url of large cover
        }

    """
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
        cover_file = current_radio.get('picture')
        cover = None
        large_cover = None
        if cover_file:
            cover = u'%s%s~%s' % (KFM_BASE_COVER, cover_file, KFM_COVER_SIZE_NORMAL)
            large_cover = u'%s%s~%s' % (KFM_BASE_COVER, cover_file, KFM_COVER_SIZE_LARGE)

        data = {
            'artist': artist,
            'name': name,
            'cover': cover,
            'large_cover': large_cover
        }

    except:
        data = None

    return data
