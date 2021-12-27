#!/usr/bin/env python3
import json
from os import environ as env
from string import Template

f_manifest = open('manifest.json')
f_template = open('template.tpl')
manifest = json.load(f_manifest)
template = f_template.read()
substitues = env | manifest

result = Template(template).safe_substitute(substitues)
print(result)

f_manifest.close()
f_template.close()
