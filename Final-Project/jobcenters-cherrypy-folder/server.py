import cherrypy
from jobcentersController import JobCenterController
from resetController import ResetController
from ratingsController import RatingsController
from job_centers_library import _job_center_database


def start_service():
    dispatcher = cherrypy.dispatch.RoutesDispatcher()

    jcdb = _job_center_database()

    jobCenterController     = jobCenterController(jcdb=jcdb) 
    resetController     = ResetController(jcdb=jcdb)
    ratingsController   = RatingsController(jcdb=jcdb)


    dispatcher.connect('job_center_get', '/dictionary/:job_center_id', controller=jobCenterController, action = 'GET_KEY', conditions=dict(method=['GET']))
    dispatcher.connect('job_center_put', '/dictionary/:job_center_id', controller=jobCenterController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('job_center_delete', '/dictionary/:job_center_id', controller=jobCenterController, action = 'DELETE_KEY', conditions=dict(method=['DELETE']))
    dispatcher.connect('job_center_index_get', '/dictionary/', controller=jobCenterController, action = 'GET_INDEX', conditions=dict(method=['GET']))
    dispatcher.connect('job_center_index_post', '/dictionary/', controller=jobCenterController, action = 'POST_INDEX', conditions=dict(method=['POST']))
    dispatcher.connect('job_center_index_delete', '/dictionary/', controller=jobCenterController, action = 'DELETE_INDEX', conditions=dict(method=['DELETE']))

    dispatcher.connect('reset_put', '/reset/:job_center_id', controller=resetController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
    dispatcher.connect('reset_index_put', '/reset/', controller=resetController, action = 'PUT_INDEX', conditions=dict(method=['PUT']))

    dispatcher.connect('rating_get', '/ratings/:job_center_id', controller=ratingsController, action = 'GET_KEY', conditions=dict(method=['GET']))


    conf = {
	'global': {
            'server.thread_pool': 5, # optional argument
	    'server.socket_host': 'localhost', # Set to localhost to work everywhere
	    'server.socket_port': 51086, #assigned port
	    },
	'/': {
	    'request.dispatch': dispatcher,
	    }
    }

    cherrypy.config.update(conf)
    app = cherrypy.tree.mount(None, config=conf)
    cherrypy.quickstart(app)

# end of start_service


if __name__ == '__main__':
    start_service()

