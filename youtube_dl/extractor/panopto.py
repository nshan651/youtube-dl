# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor


class PanoptoIE(InfoExtractor):
    IE_NAME = 'panopto'
    _VALID_URL = r'((https?:\/\/)?([a-z0-9]+[.])*(?:panopto|pro[.]panopto)([-.][a-z0-9]+)*[.]com\/(?:.*\/)?(?:Playback|embed)[\/#?]?[&?]id=([a-z0-9_-]+)(?:[&#?].*)?)'
    _TEST = {
        'url': 'https://pro.panopto.com/Panopto/Pages/Viewer.aspx?tid=db0dd9b5-c1e0-457b-bde4-afe901680800',
        'md5': '',
        'info_dict': {
            'id': 'db0dd9b5-c1e0-457b-bde4-afe901680800',
            'ext': 'mp4',
            'title': 'nishinoya rolling thunder compilation',
        }
    }
    
    def _real_extract(self, url):
        video_id = self._match_id(url)

        return {
            'id': video_id,
            'url': url,
            'title': video_id
        }

    
    
