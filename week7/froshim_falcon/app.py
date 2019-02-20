import falcon
from pathlib import Path
from wsgiref import simple_server
import jinja2
import json

env = jinja2.Environment(
    loader=jinja2.PackageLoader('app', 'templates'),
    autoescape=jinja2.select_autoescape(['html', 'xml'])
)

def load_template(name):
    return env.get_template(name)

class IndexResource:
    def on_get(self, req, resp):
        template = load_template('index.html')
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = template.render(title="Gabriel")

class RegisterResource:
    def on_post(self, req, resp):
        file_name = 'success.html'
        if 'name' not in req.params.keys() or 'dorm' not in req.params.keys():
            file_name = 'error.html'

        template = load_template(file_name)
        resp.status = falcon.HTTP_200
        resp.content_type = 'text/html'
        resp.body = template.render()

app = falcon.API()
app.req_options.auto_parse_form_urlencoded = True
app.add_route('/', IndexResource())
app.add_route('/register', RegisterResource())


# Useful for debugging problems in your API; works with pdb.set_trace(). You
# can also use Gunicorn to host your app. Gunicorn can be configured to
# auto-restart workers when it detects a code change, and it also works
# with pdb.
if __name__ == '__main__':
    httpd = simple_server.make_server('127.0.0.1', 8000, app)
    httpd.serve_forever()