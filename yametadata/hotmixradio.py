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
        'metadata_url': 'http://www.hotmixradio.fr/transfert/hotmixradio80s_liveradio.xml'
    },
    '90': {
        'metadata_url': 'http://www.hotmixradio.fr/transfert/hotmixradio90s_liveradio.xml'
    },
    'dance': {
        'metadata_url': 'http://www.hotmixradio.fr/transfert/hotmixradiodance_liveradio.xml'
    },
    'baby': {
        'metadata_url': 'http://www.hotmixradio.fr/transfert/hotmixradiobaby_liveradio.xml'
    },
    'frenchy': {
        'metadata_url': 'http://www.hotmixradio.fr/transfert/hotmixradiofrenchy_liveradio.xml'
    },
    'funky': {
        'metadata_url': 'http://www.hotmixradio.fr/transfert/hotmixradiofunky_liveradio.xml'
    },
    'hiphop': {
        'metadata_url': 'http://www.hotmixradio.fr/transfert/hotmixradiohiphop_liveradio.xml'
    },
    'hits': {
        'metadata_url': 'http://www.hotmixradio.fr/transfert/hotmixradiohits_liveradio.xml'
    },
    'hot': {
        'metadata_url': 'http://www.hotmixradio.fr/transfert/hotmixradiohot_liveradio.xml'
    },
    'lounge': {
        'metadata_url': 'http://www.hotmixradio.fr/transfert/hotmixradiolounge_liveradio.xml'
    },
    'new': {
        'metadata_url': 'http://www.hotmixradio.fr/transfert/hotmixradionew_liveradio.xml'
    },
    'rock': {
        'metadata_url': 'http://www.hotmixradio.fr/transfert/hotmixradiorock_liveradio.xml'
    },
    'sunny': {
        'metadata_url': 'http://www.hotmixradio.fr/transfert/hotmixradiosunny_liveradio.xml'
    },
    'vip': {
        'metadata_url': 'http://www.hotmixradio.fr/transfert/hotmixradiovip_liveradio.xml'
    },
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
