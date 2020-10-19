import cherrypy
import re, json
from job_centers_library import _job_center_database

class JobCenterController(object):

        def __init__(self, jcdb=None):
                if jcdb is None:
                        self.jcdb = _job_centers_database()
                else:
                        self.jcdb = jcdb

                self.jcdb.load_job_centers('Directory_Of_Job_Centers.csv')

        def GET_KEY(self, job_center_id):
                '''when GET request for /dictionary/job_center_id comes in, then we respond with json string'''
                output = {'result':'success'}
                job_center_id = int(job_center_id)


                try:
                        job_center = self.jcdb.get_movie(job_center)
                        if job_center is not None:
                                output['id'] = job_center_id
                                output['name'] = job_center[0]
                                output['borough'] = job_center[1]
                                output['address'] = job_center[2]
                                output['phone_number'] = job_center[3]
                                output['comments'] = job_center[4]
                        else:
                                output['result'] = 'error'
                                output['message'] = 'job center not found'
                except Exception as ex:
                        output['result'] = 'error'
                        output['message'] = str(ex)

                return json.dumps(output)

        def PUT_KEY(self, job_center_id):
                '''when PUT request for /dictionary/job_center_id comes in, then we change that job center in the jcdb'''
                output = {'result':'success'}
                job_center_id = int(job_center_id)

                data = json.loads(cherrypy.request.body.read().decode('utf-8'))

                job_center = list()
                job_center.append(data['name'])
                job_center.append(data['borough'])
                job_center.append(data['address'])
                job_center.append(data['phone_number'])
                job_center.append(data['comments'])

                self.jcdb.set_job_center(job_center_id, job_center)

                return json.dumps(output)

        def DELETE_KEY(self, job_center_id):
                '''when DELETE for /dictionary/dictionary_id comes in, we remove that job center from jcdb'''
                output = {'result': 'success'}
                job_center_id = int(job_center_id)
                self.jcdb.delete_movie(job_center_id)
                return json.dumps(output)

        def GET_INDEX(self):
                '''when GET request for /dictionary/ comes in, we respond with all the job center information in a json str'''
                output = {'result':'success'}
                output['job_center'] = []

                try:
                        for jcid in self.jcdb.get_job_centers():
                                job_center = self.jcdb.get_job_center(jcid)
                                djob_center = {'id':jcid, 'name':job_center[0],
                                    'borough':job_center[1], 'address': job_center[2], 'phone_number': job_center[3], 'comments': job_center[4]}
                                output['job_center'].append(djob_center)
                except Exception as ex:
                        output['result'] = 'error'
                        output['message'] = str(ex)

                return json.dumps(output)

        def POST_INDEX(self):
                '''when POST for /dictionary/ comes in, we take parameters from body of request, and respond with the new jcid and more'''
                output = {'result':'success'}
                data = json.loads(cherrypy.request.body.read().decode('utf-8'))
                
                jcid = 0
                for key in self.jcdb.movie_names:
                   jcid = max(key, jcid)
                jcid+= 1
                job_center = [data['name'], data['borough'], data['address'], data['phone_number'], data['comments']]
                self.jcdb.set_movie(jcid, job_center)
                output['id'] = jcid
                return json.dumps(output)



        def DELETE_INDEX(self):
                '''when DELETE for /dictionary/ comes in, we remove each existing job center from jcdb object'''
                self.jcdb.boroughs = dict()
                self.jcdb.job_center_names = dict()
                self.jcdb.addresses = dict()
                self.jcdb.phone_numbers = dict()
                self.jcdb.comments = dict()
                output = {'result': 'success'}
                return json.dumps(output)

                
