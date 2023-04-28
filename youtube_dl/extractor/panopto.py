# coding: utf-8
from __future__ import unicode_literals

from .common import InfoExtractor
import re

class PanoptoIE(InfoExtractor):
    IE_NAME = 'panopto'
    # _VALID_URL = r'https?://(?:[^/]+\.)?panopto\.com/Panopto/Pages/Viewer\.aspx\?.*?id=(?P<id>[0-9a-f]+)'

    _VALID_URL = r'(?:https?://)?(?P<host>.*?\.)?panopto\.com/Panopto/Pages/Viewer\.aspx\?(?:.*?&)?(?:id=|p=|pid=|aid=|tid=|folderID=)(?P<id>[0-9a-f\-]+)'
    # _TEST = {
    #     'url': 'https://pro.panopto.com/Panopto/Pages/Viewer.aspx?tid=db0dd9b5-c1e0-457b-bde4-afe901680800',
    #     'md5': '',
    #     'info_dict': {
    #         'id': 'db0dd9b5-c1e0-457b-bde4-afe901680800',
    #         'ext': 'mp4',
    #         'title': 'nishinoya rolling thunder compilation',
    #     }
    # }
    _TESTS = [{
        'url': 'https://demo.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=01234567-89ab-cdef-0123-456789abcdef',
        'info_dict': {
            'id': '01234567-89ab-cdef-0123-456789abcdef',
            'ext': 'mp4',
            'title': 'Video title',
        },
        'params': {
            'skip_download': True,
        },
    }]
    # _VIDEO_URL = r'https://.*\.cloudfront\.net/\d+/[0-9a-f]+/\d+/\d+/\d+/\d+/(?P<id>[0-9a-f]+)\.mp4'
    # _VIDEO_URL = r'https?://.*?\.cloud\.panopto\.eu/Panopto/Podcast/.*?/.*?(?P<id>[0-9a-f]+)\.mp4'

    # _VIDEO_URL = r'https?://(?P<host>[^/]*?\.)?panopto\.com/Panopto/.*?(?:|type=mp4|disp=inline)/(?:[0-9a-f]+-)?(?P<id>[0-9a-f]+)\.mp4'
    _VIDEO_URL = r'https?://streams\.cloud\.panopto\.eu/.*?(?P<id>[0-9a-f]+)\.mp4'


    def _real_extract(self, url):
        mobj = re.match(self._VALID_URL, url)
        video_id = mobj.group('id')
        print("VIDEO ID is: ", video_id)
        webpage = self._download_webpage(url, video_id)
        print("MOBJ MATCH is: ", mobj)
        # print("WEBPAGE is: ", webpage)
        # mobj = re.search(self._VIDEO_URL, webpage)
        print("MOBJ SEARCH is: ", mobj)
        if mobj:
            source_url = mobj.group(0)
            title = self._og_search_title(webpage)
            return {
                'id': video_id,
                'url': source_url,
                'title': title,
                'ext': 'mp4',
            }
        else:
            self.report_warning('Unable to extract video URL')
            return None
