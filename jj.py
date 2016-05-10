from jinja2 import Template, Environment, PackageLoader


env = Environment(loader=PackageLoader('app', 'templates'))

home = env.get_template('child.html')
bubblemap = env.get_template('map.html')
about = env.get_template('about.html')

with open('index.html', 'w') as f:
    f.write(home.render())

with open('map.html', 'w') as f:
    f.write(bubblemap.render())

with open('about.html', 'w') as f:
    f.write(about.render())
