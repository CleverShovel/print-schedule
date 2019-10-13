from jinja2 import Environment, FileSystemLoader
import imgkit
import json
import sys

input_file = open(sys.argv[1], "r")
output_file = sys.argv[2]

lessons = json.load(input_file)

templateLoader = FileSystemLoader(searchpath="./")
templateEnv = Environment(loader=templateLoader)

template = templateEnv.get_template('schedule_wo_bootstrap.html')
res = template.render(lessons=lessons)

# css = './css/bootstrap.min.css'
imgkit.from_string(res, output_file, options={
   'format': 'png',
    # 'crop-h': '300',
    'crop-w': '310',
    'crop-x': '3',
    'crop-y': '3'
})