try:
  from urllib import unquote
except:
  # python 3
  from urllib.parse import unquote

from notebook.utils import url_path_join
from notebook.base.handlers import IPythonHandler
from notebook.services.contents.handlers import ContentsHandler

class Post(IPythonHandler):
  def post(self):
    notebook = unquote(self.request.path[14:]);

    self.request.method = 'PUT';
    self.request.path = '/api/contents/' + notebook;

    ContentsHandler(self.application,self.request)._execute(
      [t(self.request) for t in self.application.transforms], notebook
    );

def load_jupyter_server_extension(app):
  web_app = app.web_app
  host_pattern = '.*$'
  post_to_put_pattern= url_path_join(web_app.settings['base_url'], '/post/.*')
  web_app.add_handlers(host_pattern, [(post_to_put_pattern, Post)])
