"""
Takes a jsonresume file and formats in in markdown
"""
import os
import json
from jinja2 import Environment, FileSystemLoader

dirname = os.path.dirname(os.path.abspath(__file__))

with open('resume.json') as fd:
    resume = json.loads(fd.read())
env = Environment()
loader = FileSystemLoader(dirname)
tmpl  = loader.load(env, 'resume.tmpl')
context=dict(resume)
print tmpl.render(context)
