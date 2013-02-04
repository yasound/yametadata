"""
hotmixradio parser

example of metadata::

    <rol_notification>
        <name>Hotmixradio - 80s</name>
        <timeZone>Europe/Paris</timeZone>
        <url>http://www.hotmixradio80s.fr</url>
        <onair>
            <start>2013-02-04 14:23:29</start>
            <title>
                <![CDATA[ Running Up That Hill ]]>
            </title>
            <artist>
                <![CDATA[ KATE BUSH ]]>
            </artist>
            <album/>
                <duration>299</duration>
            <info>
                http://www.hotmixradio.fr/titre/kate-bush/running-up-that-hill
            </info>
            <cover>
                http://www.hotmixradio.fr/images/hmr_titre/KATE BUSH - Running Up That Hill.jpg
            </cover>
            <music>S</music>
            <comment/>
        </onair>
    </rol_notification>

"""

import xmltodict
import requests


HOTMIX_DATA = {
    '80': {
        'stream': 'http://streamingads.hotmixradio.fm/hotmixradio-80-128.mp3',
        'metadata_url': 'http://www.hotmixradio.fr/transfert/hotmixradio80s_liveradio.xml'
    }
}


def find_metadata(name):
    """Return the current song.
    the returned data is a dict::

        dict = {
            'name': 'foo', # title
            'artist': 'bla' # artist name
            'album': 'artist' # artist name
            'cover': 'http://cover_normal', # url of normal cover
        }

    """

    data = HOTMIX_DATA.get(name)
    if data is None:
        return None

    try:
        r = requests.get(data.get('metadata_url'))
    except:
        return None

    content = None
    try:
        content = r.content.encode('utf-8')
    except:
        content = r.content

    try:
        data = xmltodict.parse(content)
        onair = data.get('rol_notification', {}).get('onair', {})
        name = onair.get('title')
        artist = onair.get('artist')
        album = onair.get('album')
        cover = onair.get('cover')
    except:
        data = None

    dict = {
        'name': name,
        'artist': artist,
        'album': album,
        'cover': cover,
    }

    return dict
