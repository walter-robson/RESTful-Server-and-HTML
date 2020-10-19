import unittest
import requests
import json

class TestJobCentersIndex(unittest.TestCase):

    SITE_URL = 'http://student00.cse.nd.edu:51086' # replace with your assigned port id
    print("Testing for server: " + SITE_URL)
    JOB_CENTER_URL = SITE_URL + '/dictionary/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        jc = {}
        r = requests.put(self.RESET_URL, json.dumps(jc))

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_job_center_index_get(self):
        self.reset_data()
        r = requests.get(self.JOB_CENTER_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        testjobcenter = {}
        job_centers = resp['job_centers']
        for job_center in job_centers:
            if job_center['id'] == 9:
                testjobcenter = job_center

        self.assertEqual(testjobcenter['name'], 'Dekalb')
        self.assertEqual(testjobcenter['borough'], 'Brooklyn')

    def test_job_center_index_post(self):
        self.reset_data()

        jc = {}
        jc['name'] = 'ABC'
        jc['borough'] = 'QUEENS'
        jc['address'] = '100 manhattan ave'
        jc['phone_number'] = '571-420-3987'
        jc['comments'] = 'pretty slick'
        jc['id'] = 30
        r = requests.post(self.JOB_CENTER_URL, data = json.dumps(jc))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        self.assertEqual(resp['id'], 30)
        r = requests.get(self.JOB_CENTER_URL + str(resp['id']))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['name'], jc['name'])
        self.assertEqual(resp['borough'], jc['borough'])

    def test_job_center_index_delete(self):
        self.reset_data()

        jc = {}
        r = requests.delete(self.JOB_CENTER_URL, data = json.dumps(jc))
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.JOB_CENTER_URL)
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        job_centers = resp['job_centers']
        self.assertFalse(job_centers)

if __name__ == "__main__":
    unittest.main()

