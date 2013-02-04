# -*- coding: utf-8 -*-

"""
yametadata
~~~~~~~~~~

:copyright: (c) 2012, 2013 Yasound SAS.
:license: Proprietary see LICENSE for more details.

"""

__title__ = 'yametadata'
__version__ = '0.2'
__author__ = 'Jérôme Blondon'
__license__ = 'Proprietary'
__copyright__ = 'Copyright 2012 Yasound SAS'


import settings
import kfm
import radioways
import franceinter
import hotmixradio


def find_metadata(radio_type, *args, **kwargs):
    if radio_type == settings.RADIO_RADIOWAYS:
        radio_id = kwargs.get('radio_id')
        return radioways.find_metadata(radio_id)
    elif radio_type == settings.RADIO_KFM:
        return kfm.find_metadata()
    elif radio_type == settings.RADIO_FRANCE_INTER:
        return franceinter.find_metadata()
    elif radio_type == settings.RADIO_HOTMIXRADIO:
        return hotmixradio.find_metadata(*args, **kwargs)
    return None
