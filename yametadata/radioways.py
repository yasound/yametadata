import xml2dic
import requests

def find_metadata(radio_id):
    url = 'http://www.radioways.com/com/php/yasound.php'
    params = {
        'metadataId': radio_id
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
        data = xml2dic.as_dict(content)
    except:
        data = None

    return data
