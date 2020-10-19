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
        #TODO complete this test
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')
        r = requests.get(self.SITE_URL +  '/movies/')
        resp = json.loads(r.content.decode())
        movies = resp['movies']
        self.assertEqual(movies[0]['title'], 'Toy Story (1995)')


    def test_put_reset_key(self):
        m = {}
        r = requests.put(self.RESET_URL, json.dumps(m))

        movie_id = 1
        m['title'] = 'movie title'
        m['genres'] = 'movive genres'
        r = requests.put(self.SITE_URL + '/movies/' + str(movie_id), data=json.dumps(m))

        m = {}
        r = requests.put(self.RESET_URL + str(movie_id), data=json.dumps(m))
        resp = json.loads(r.content.decode())
        self.assertEqual(resp['result'], 'success')

        r = requests.get(self.SITE_URL + '/movies/')
        resp = json.loads(r.content.decode())
        movies = resp['movies']
        self.assertEqual(movies[0]['title'], 'Toy Story (1995)')
	

if __name__ == "__main__":
    unittest.main()

