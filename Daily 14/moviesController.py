import cherrypy
import re, json
from movies_library import _movie_database

class MovieController(object):

        def __init__(self, mdb=None):
                if mdb is None:
                        self.mdb = _movie_database()
                else:
                        self.mdb = mdb

                self.mdb.load_movies('movies.dat')

        def GET_KEY(self, movie_id):
                '''when GET request for /movies/movie_id comes in, then we respond with json string'''
                output = {'result':'success'}
                movie_id = int(movie_id)


                try:
                        movie = self.mdb.get_movie(movie_id)
                        if movie is not None:
                                output['id'] = movie_id
                                output['title'] = movie[0]
                                output['genres'] = movie[1]
                        else:
                                output['result'] = 'error'
                                output['message'] = 'movie not found'
                except Exception as ex:
                        output['result'] = 'error'
                        output['message'] = str(ex)

                return json.dumps(output)

        def PUT_KEY(self, movie_id):
                '''when PUT request for /movies/movie_id comes in, then we change that movie in the mdb'''
                output = {'result':'success'}
                movie_id = int(movie_id)

                data = json.loads(cherrypy.request.body.read().decode('utf-8'))

                movie = list()
                movie.append(data['title'])
                movie.append(data['genres'])

                self.mdb.set_movie(movie_id, movie)

                return json.dumps(output)

        def DELETE_KEY(self, movie_id):
                '''when DELETE for /movies/movie_id comes in, we remove just that movie from mdb'''
                output = {'result': 'success'}
                movie_id = int(movie_id)
                self.mdb.delete_movie(movie_id)
                return json.dumps(output)

        def GET_INDEX(self):
                '''when GET request for /movies/ comes in, we respond with all the movie information in a json str'''
                output = {'result':'success'}
                output['movies'] = []

                try:
                        for mid in self.mdb.get_movies():
                                movie = self.mdb.get_movie(mid)
                                dmovie = {'id':mid, 'title':movie[0],
                                                'genres':movie[1]}
                                output['movies'].append(dmovie)
                except Exception as ex:
                        output['result'] = 'error'
                        output['message'] = str(ex)

                return json.dumps(output)

        def POST_INDEX(self):
                '''when POST for /movies/ comes in, we take title and genres from body of request, and respond with the new movie_id and more'''
                output = {'result':'success'}
                data = json.loads(cherrypy.request.body.read().decode('utf-8'))
                
                mid = 0
                for key in self.mdb.movie_names:
                   mid = max(key, mid)
                mid+= 1
                movie = [data['title'], data['genres']]
                self.mdb.set_movie(mid, movie)
                output['id'] = mid
                return json.dumps(output)



        def DELETE_INDEX(self):
                '''when DELETE for /movies/ comes in, we remove each existing movie from mdb object'''
                self.mdb.movie_names = dict()
                self.mdb.movie_genres = dict()
                self.mdb.movie_ratings = dict()
                output = {'result': 'success'}
                return json.dumps(output)

                
