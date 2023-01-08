from gevent import monkey

from settings import config

monkey.patch_all()

from gevent.pywsgi import WSGIServer
from main_dash import server as application

http_server = WSGIServer(('', config.app_port), application)
http_server.serve_forever()
