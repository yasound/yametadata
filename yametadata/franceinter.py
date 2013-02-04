import datetime
import requests

FRANCE_INTER_URL = 'http://www.franceinter.fr/sites/default/files/rf_player/player-direct.json?_='

def find_metadata():
    from pyquery import PyQuery as pq
    random = datetime.datetime.now().strftime('%s')
    url = '%s%s' % (FRANCE_INTER_URL, random)
    try:
        r = requests.get(url)
    except:
        return None

    data = r.json
    d = pq(data.get('donnees_associees'))
    titles = d('div').filter('.metas')

    title = titles.eq(0).text()
    subtitle = titles.eq(1).text()

    dict = {
        'name': title,
        'artist': subtitle,
    }

    return dict
