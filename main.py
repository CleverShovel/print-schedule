from jinja2 import Environment, FileSystemLoader
import imgkit
import json
import sys

lessons = json.load(open(sys.argv[1], "r"))

templateLoader = FileSystemLoader(searchpath="./")
templateEnv = Environment(loader=templateLoader)

template = templateEnv.get_template('schedule_wo_bootstrap.html')
res = template.render(lessons=lessons)

# css = './css/bootstrap.min.css'
imgkit.from_string(res, 'out.jpg', options={
   'format': 'png',
    # 'crop-h': '300',
    'crop-w': '310',
    'crop-x': '3',
    'crop-y': '3'
})