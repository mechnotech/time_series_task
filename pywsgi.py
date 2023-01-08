from gevent import monkey

from settings import Settings

monkey.patch_all()

from gevent.pywsgi import WSGIServer
from app import server as application

settings = Settings()
http_server = WSGIServer(('', settings.app_port), application)
http_server.serve_forever()
