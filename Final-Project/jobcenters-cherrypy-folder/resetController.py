import cherrypy
import re, json
from job_centers_library import _job_center_database

class ResetController(object):

    def __init__(self, jcdb=None):
        if jcdb is None:
            self.jcdb = _job_center_database()
        else:
            self.jcdb = jcdb


    def PUT_INDEX(self):
        '''when PUT request comes in to /reset/ endpoint, then the movie database is reloaded'''
        output = {'result':'success'}

        #data = json.loads(cherrypy.request.body.read().decode())

        self.jcdb.__init__()
        self.jcdb.load_job_centers('Directory_Of_Job_Centers.csv')

        return json.dumps(output)

    def PUT_KEY(self, job_center_id):
        '''when PUT request comes in for /reset/job_center_id endpoint, then that job center is reloaded and updated in jcdb'''
        output = {'result':'success'}
        jcid = int(job_center_id)

        try:
            data = json.loads(cherrypy.request.body.read().decode())

            jcdbtmp = _job_center_database()
            jcdbtmp.load_job_centers('Directory_Of_Job_Centers.csv')

            job_center = jcdbtmp.get_job_center(jcid)
            
            self.jcdb.set_job_center(jcid, job_center)


        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output)

