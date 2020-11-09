import cherrypy
from jobCentersController import JobCenterController
from resetController import ResetController
from commentsController import CommentsController
from job_centers_library import _job_center_database

class optionsController:
    def OPTIONS(self, *args, **kwargs):
        return ""

def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"


def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    jcdb = _job_center_database()

    jobCenterController     = JobCenterController(jcdb=jcdb) 
    resetController     = ResetController(jcdb=jcdb)
    commentsController   = CommentsController(jcdb=jcdb)


    dispatcher.connect('job_center_get', '/dictionary/:job_center_id', controller=jobCenterController, action = 'GET_KEY', conditions=dict(method=['GET']))
    dispatcher.connect('job_center_put', '/dictionary/:job_center_id', controller=jobCenterController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('job_center_delete', '/dictionary/:job_center_id', controller=jobCenterController, action = 'DELETE_KEY', conditions=dict(method=['DELETE']))
    dispatcher.connect('job_center_index_get', '/dictionary/', controller=jobCenterController, action = 'GET_INDEX', conditions=dict(method=['GET']))
    dispatcher.connect('job_center_index_post', '/dictionary/', controller=jobCenterController, action = 'POST_INDEX', conditions=dict(method=['POST']))
    dispatcher.connect('job_center_index_delete', '/dictionary/', controller=jobCenterController, action = 'DELETE_INDEX', conditions=dict(method=['DELETE']))

    dispatcher.connect('reset_put', '/reset/:job_center_id', controller=resetController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('reset_index_put', '/reset/', controller=resetController, action = 'PUT_INDEX', conditions=dict(method=['PUT']))

    dispatcher.connect('comment_get', '/comments/:job_center_id', controller=commentsController, action = 'GET_KEY', conditions=dict(method=['GET']))
    dispatcher.connect('comment_put', '/comments/:job_center_id', controller=commentsController, action = 'PUT_KEY', conditions=dict(method=['PUT']))

    # CORS related options connections
    dispatcher.connect('dictionary_key_options', '/dictionary/:job_center_id', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))

    dispatcher.connect('dictionary_options', '/dictionary/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    dispatcher.connect('reset_key_options', '/reset/:job_center_id', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))

    dispatcher.connect('reset_options', '/reset/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))

    dispatcher.connect('comments_options', '/comments/:job_center_id', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
    conf = {
	'global': {
            'server.thread_pool': 5, # optional argument
			'server.socket_host': 'student04.cse.nd.edu', # Set to localhost to work everywhere
	    'server.socket_port': 51086, #assigned port
	    },
	'/': {
	    'request.dispatch': dispatcher,
        'tools.CORS.on':True,
	    }
    }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

# end of start_service


if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
    start_service()

