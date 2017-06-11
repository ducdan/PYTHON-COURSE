import unittest
from flask import json
from flask_testing import TestCase
from project import app
from project.models.model import db, Song, File
from project.controllers.control import createData
from io import BytesIO

UPLOAD_FOLDER = app.root_path + '/upload_file'

class BaseTestCase(TestCase):
    def create_app(self):
        app.config.from_pyfile('config.cfg')
        return app

    def setUp(self):
        db.create_all()
        createData(File(id=12, filename='Have a nice day.mp3'))


    def tearDown(self):
        db.session.remove()
        db.drop_all()

class CheckAPI(BaseTestCase):
    # Get data from database
    def test_get_api_songs(self):
        response = self.client.get('/api/songs', content_type='application/json')
        self.assert200(response)
        self.assertIn(b'"id": 12', response.data)
        self.assertIn(b'"Have a nice day.mp3"', response.data)

    def test_post_api_songs(self):
        response = self.client.post(
            '/api/songs',
            data=json.dumps( {'file':{'id': 15 ,'name': 'Miss you.mp3'}}))
        self.assert200(response)
        self.assertIn(b'Added song', response.data)

        response = self.client.post(
            '/api/songs',
            data=json.dumps( {'file':{'id': 12 ,'name': 'Miss you.mp3'}}))
        self.assert200(response)
        self.assertIn(b'File exists in database', response.data)

    def test_add_songs(self):
        response = self.client.post(
            '/api/songs/add',
            data={'id_song': 20 ,'name_song': 'Miss you.mp3'})
        self.assert200(response)
        self.assertIn(b'Added song', response.data)

        response = self.client.post(
            '/api/songs/add',
            data={'id_song': 20 ,'name_song': 'Miss you.mp3'})
        self.assert200(response)
        self.assertIn(b'File exists in database', response.data)

class CheckUpload(BaseTestCase):
    def test_get_uploaded_file(self):
        path = UPLOAD_FOLDER + '/' + 'test.txt'
        with open(path, "wb") as f:
            f.write(b"File contents")

        response = self.client.get('/uploads/test.txt')

        self.assert200(response)
        self.assertEqual(response.mimetype, "text/plain")
        self.assertEqual(response.data, b"File contents")

    def test_file_upload(self):
        data = {
            "fileToUpload": (BytesIO(b'File contents'), 'test2.txt')
        }

        response = self.client.post("/api/files",
                                    data=data,
                                    content_type="multipart/form-data",
                                    headers=[("Accept", "application/json")])

        test2_content = self.client.get('/uploads/test2.txt')

        self.assertIsNotNone(test2_content)
        self.assertEqual(test2_content.data, b'File contents')


if __name__ == '__main__':
    unittest.main()