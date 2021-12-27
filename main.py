#!/usr/bin/env python3
import json
from os import environ as env
from string import Template

f_manifest = open('manifest.json', 'r')
f_output = open('output.txt', 'w')
f_template = open('template.tpl', 'r')
manifest = json.load(f_manifest)
template = f_template.read()
# Merging env vars with manifest dictionary
substitues = env | manifest

result = Template(template).safe_substitute(substitues)
print(result)
f_output.write(result)

# Closing all opened files
f_manifest.close()
f_output.close()
f_template.close()
