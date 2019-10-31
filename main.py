#!/usr/bin/env python3

from jinja2 import Environment, FileSystemLoader
import imgkit
import json
import sys
from os import path
from configparser import ConfigParser


input_file = open(sys.argv[1], "r")
output_file = sys.argv[2]


cur_folder = path.dirname(path.realpath(__file__))

settings_file = path.join(cur_folder, 'settings.ini')
def_settings_file = path.join(cur_folder, 'settings.ini.default')

config = ConfigParser()
config.read(settings_file if path.isfile(settings_file) else def_settings_file)

general = config['GENERAL']
template_folder = general['TEMPLATE_FOLDER']
options_file = open(general['OPTIONS_FILE'], "r")

css_folder = path.join(cur_folder, 'css')
options = json.load(options_file)

js_dict = json.load(input_file)
date = js_dict["date"]
lessons = js_dict["lessons"]

templateLoader = FileSystemLoader(searchpath=template_folder)
templateEnv = Environment(loader=templateLoader)
templateEnv.trim_blocks = True
templateEnv.lstrip_blocks = True

def max_length_of_groups(groups):
    return max(map(lambda x : max(map(lambda y: y['subgroup'], x.list)), groups))

def add_empty_subgroups(lessons):
    max_subgroup = max(int(x['subgroup']) for x in lessons)
    if max_subgroup == 0:
        return lessons
    subgroups_lessons = {int(x['subgroup']): x for x in lessons}
    for i in range(1, max_subgroup + 1):
        if i not in subgroups_lessons:
            subgroups_lessons[i] = None
    return [y for (x,y) in sorted(subgroups_lessons.items())]

templateEnv.filters['add_empty_subgroups'] = add_empty_subgroups
templateEnv.filters['max_length_of_groups'] = max_length_of_groups

template = templateEnv.get_template('schedule.html')
res = template.render(date=date, lessons=lessons)

css = [path.join(css_folder, 'w3.css'), path.join(css_folder, 'style.css')]
imgkit.from_string(res, output_file, options=options, css=css)
