import unittest
import requests
import json

class TestJobCenters(unittest.TestCase):

    SITE_URL = 'localhost:51086' # replace with your port number and 
    print("testing for server: " + SITE_URL)
    JOB_CENTER_URL = SITE_URL + '/dictionary/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        jc = {}
        r = requests.put(self.RESET_URL, data = json.dumps(jc))


    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_job_centers_get_key(self):
        self.reset_data()
        job_center_id = 9
        r = requests.get(self.JOB_CENTER_URL + str(job_center_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['name'], 'Dekalb')
        self.assertEqual(resp['borough'], 'Brooklyn')

    def test_job_centers_put_key(self):
        self.reset_data()
        job_center_id = 10

        r = requests.get(self.JOB_CENTER_URL + str(job_center_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['name'], 'Dekalb')
        self.assertEqual(resp['borough'], 'Brooklyn')

        jc = {}
        jc['name'] = 'ABC'
        jc['borough'] = 'QUEENS'
        r = requests.put(self.JOB_CENTER_URL + str(job_center_id), data = json.dumps(jc))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.JOB_CENTER_URL + str(job_center_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['name'], jc['name'])
        self.assertEqual(resp['borough'], jc['borough'])

    def test_job_centers_delete_key(self):
        self.reset_data()
        job_center_id = 10

        jc = {}
        r = requests.delete(self.JOB_CENTER_URL + str(job_center_id), data = json.dumps(jc))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.JOB_CENTER_URL + str(job_center_id))
        self.assertTrue(self.is_json(r.content.decode('utf-8')))
        resp = json.loads(r.content.decode('utf-8'))
        self.assertEqual(resp['result'], 'error')
        #self.assertEqual(resp['message'], 'movie not found')

if __name__ == "__main__":
    unittest.main()

