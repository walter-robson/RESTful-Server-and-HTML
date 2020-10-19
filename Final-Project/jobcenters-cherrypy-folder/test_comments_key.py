import unittest
import requests
import json

class TestComments(unittest.TestCase):

    SITE_URL = 'http://student00.cse.nd.edu:51086' # replace with your port id
    print("Testing for server: " + SITE_URL)
    RATINGS_URL = SITE_URL + '/comments/'
    RESET_URL = SITE_URL + '/reset/'

    def reset_data(self):
        j = {}
        r = requests.put(self.RESET_URL)

    def is_json(self, resp):
        try:
            json.loads(resp)
            return True
        except ValueError:
            return False

    def test_ratings_get_key(self):
        self.reset_data()
        job_center_id = 9

        r = requests.get(self.RATINGS_URL + str(job_center_id))
        #print("response is " + str(r.content.decode())) #debug
        self.assertTrue(self.is_json(r.content.decode()))
        resp = json.loads(r.content.decode())
        #self.assertEqual(resp['rating'], 3.945731303772336) # this is the value when user data is also considered
        #self.assertEqual(resp['rating'], 0.0)
        #self.assertEqual(resp['job_'], movie_id)

if __name__ == "__main__":
    unittest.main()

