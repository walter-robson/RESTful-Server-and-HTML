import cherrypy
import re, json
from job_centers_library import _job_center_database

class CommentsController(object):

    def __init__(self, jcdb=None):
        if jcdb is None:
            self.jcdb = _job_center_database()
        else:
            self.jcdb = jcdb


    def GET_KEY(self, job_center_id):
        '''when GET request comes in for /comments/job_center_id endpoint, then we respond with the comments'''
        output = {'result':'success'}
        output['job_center_name'] = job_center_id
        for i, jcname in self.jcdb.job_center_names.items():
            if jcname.lower() == job_center_id.lower():
                output['comments'] = self.jcdb.get_comments(i)

        return json.dumps(output)

    def PUT_KEY(self, job_center_id):
        ''' When PUT request for /dictionary/job_center_id comes in, we append a new comment to that job center in jcdb'''
        data = json.loads(cherrypy.request.body.read().decode('utf-8'))
        comment = data['comment']
        output = {'result': 'success'}
        for i, jcname in self.jcdb.job_center_names.items():
            if jcname.lower() == job_center_id.lower():
                self.jcdb.set_comment(job_center_id, comment)
        return json.dumps(output)

