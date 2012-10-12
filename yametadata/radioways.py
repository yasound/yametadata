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

    if content.startswith("<?xml version='1.0' encoding='windows-12'?>"):
        # special case when encoding is broken
        left = content[len("<?xml version='1.0' encoding='windows-12?>"):]
        content = "<?xml version='1.0' encoding='windows-1252'?" + left

    try:
        data = xml2dic.as_dict(content)
    except:
        data = None

    return data
