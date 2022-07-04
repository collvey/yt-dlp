#!/usr/bin/env python3

# Allow direct execution
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from test.helper import FakeYDL
from yt_dlp import YoutubeDL
from yt_dlp.extractor import YoutubeIE

class TestYouTubeOffline(unittest.TestCase):
    _URL = ['https://www.youtube.com/watch?v=w6WNAtHiQmI']

    def test_youtube_extract(self):
        params = {'paths': {'home': '.\\downloaded\\'}}
        dl = YoutubeDL(params)
        # Extract video info 
        ie = YoutubeIE(dl)
        result = ie.extract(self._URL[0])
        print(result)

    def test_youtube_download(self):
        params = {'paths': {'home': '.\\downloaded\\'}}
        dl = YoutubeDL(params)
        # Download video
        dl.download(self._URL)

if __name__ == '__main__':
    unittest.main()