from jsmin import jsmin
import os


jsfiles_dir = os.path.join(
    os.path.realpath(os.path.dirname(__file__)),
    'nilms/static/site/js'
)

final_jsfile = os.path.join(jsfiles_dir, 'packed.js')

jsfiles = [
    'wget.js',
    'wpost.js',
    'initializer.js',
    'utils.js',
    'save.js'
]

jscontents = ''

for fname in jsfiles:
    with open(os.path.join(jsfiles_dir, fname)) as _file:
        jscontents += jsmin(_file.read())
    _file.close()

with open(final_jsfile, 'w+') as _file:
    _file.write(jscontents)
_file.close()
