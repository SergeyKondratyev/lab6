from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from webob import Request, Response
from jinja2 import Environment, FileSystemLoader

items = [
'app.js',
'react.js',
'leaflet.js',
'D3.js',
'moment.js',
'math.js',
'main.css',
'bootstrap.css',
'normalize.css',
]
js = []
css = []

for item in items:
  dividedOne, dividedTwo = item.split('.')
  if dividedTwo == 'js':
    js.append(item)
  elif dividedTwo == 'css':
    css.append(item)

env = Environment(loader=FileSystemLoader('.'))

# Вывод index.html
def index(request):
  template = env.get_template('index.html')
  return Response(template.render(scripts=js, styles=css))

# Вывод aboutme.html
def about(request):
  template = env.get_template('about/aboutme.html')
  return Response(template.render(scripts=js, styles=css))

def main():
  config = Configurator() 
  config.add_route('index', '/')
  config.add_view(index, route_name='index')
  config.add_route('about', '/about')
  config.add_view(about, route_name='about')
  app = config.make_wsgi_app()
  return app

if __name__ == '__main__':
  app = main()
  make_server('0.0.0.0', 80, app).serve_forever()