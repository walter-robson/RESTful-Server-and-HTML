import unittest
import requests
import json

class TestReset(unittest.TestCase):

    SITE_URL = 'localhost:51086' # replace with your port id
    print("Testing for server: " + SITE_URL)
    RESET_URL = SITE_URL + '/reset/'

    def test_put_reset_index(self):
        m = {}
        r = requests.put(self.RESET_URL, json.dumps(m))

        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        r = requests.get(self.SITE_URL +  '/dictionary/')
        resp = json.loads(r.content.decode())
        job_centers = resp['job_center']
        self.assertEqual(job_centers[0]['name'], 'Concourse')


    def test_put_reset_key(self):
        j = {}
        r = requests.put(self.RESET_URL, json.dumps(j))

        job_center_id = 1
        j['name'] = 'job center title'
        j['borough'] = 'hip borough'
        j['address'] = '100 manhattan ave'
        j['phone_number'] = '571-420-3987'
        j['comments'] = 'this is a job center comment'
        r = requests.put(self.SITE_URL + '/dictionary/' + str(job_center_id), data=json.dumps(j))

        j = {}
        r = requests.put(self.RESET_URL + str(movie_id), data=json.dumps(m))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.SITE_URL + '/dictionary/')
        resp = json.loads(r.content.decode())
        job_centers = resp['job_centers']
        self.assertEqual(job_center[0]['name'], 'Concourse')

if __name__ == "__main__":
    unittest.main()

