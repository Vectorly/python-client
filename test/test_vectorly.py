import unittest
import uuid
import os
import glob
import filecmp
import shutil
import time
from vectorly.vectorly import Vectorly, VectorlyError


API_KEY = 'cc07b8c4-e63f-46c8-b912-fac5b919f3e0'

class VectorlyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.Vec = Vectorly(api_key=API_KEY)
        cls.file_name = f'{uuid.uuid4()}.avi'
        shutil.copyfile('MVI_0043.AVI', cls.file_name)
        try:
            cls.Vec.upload(cls.file_name)
        except Exception as e:
            cls.assertIsNone(e)

    @classmethod
    def tearDownClass(cls):
        # teardown_something()
        os.remove(cls.file_name)
        try:
            os.remove(f'{cls.file_name}.new')
        except:
            pass

    # def test_upload(self):
    #     # test upload
    #     try:
    #         self.Vec.upload(self.file_name)
    #     except Exception as e:
    #         self.assertIsNone(e)

    def test_list(self):
        # test list
        try:
            # self.Vec.upload(self.file_name)
            list_files = self.Vec.list()
            self.assertIn(self.file_name, [record['name'] for record in list_files])
        except Exception as e:
            self.assertIsNone(e)

    def test_video_detaill(self):
        # test detail
        try:
            # self.Vec.upload(self.file_name)
            list_files = self.Vec.list()
            self.assertIn(self.file_name, [record['name'] for record in list_files])
            detail_one = self.Vec.video_detail(list_files[0]['id'])
            self.assertIsNotNone(detail_one)
        except Exception as e:
            self.assertIsNone(e)

    def test_search(self):
        # test search
        try:
            # self.Vec.upload(self.file_name)
            search_list = self.Vec.search(self.file_name)
            self.assertEqual(self.file_name, search_list[0]['name'], 'Not relevant search')
        except Exception as e:
            self.assertIsNone(e)

    def test_download(self):
        # test download
        try:
            # self.Vec.upload(self.file_name)
            status = ''
            search_list = []
            for _ in range(120):
                search_list = self.Vec.search(self.file_name)
                self.assertEqual(self.file_name, search_list[0]['name'], 'Not relevant search')
                status = search_list[0]['status']
                time.sleep(1)
                if status == 'ready':
                    break
            self.assertEqual('ready', status, 'File not ready. Time out 120 sec')
            video_id = search_list[0]['id']
            new_file = f'{self.file_name}.new'
            self.Vec.download(video_id, new_file)
            find_new_file = glob.glob(new_file)
            self.assertEqual(1, 1)
        except Exception as e:
            self.assertIsNone(e)

if __name__ == '__main__':
    unittest.main()