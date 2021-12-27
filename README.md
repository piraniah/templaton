# templaton
This is a simple python script to generate output.txt file based on a template.tpl and manifests.json. Script allows replacing values with env vars that can be extracted from vault or and from manifest files.
Required files:
* manifest.json (can be empty {})
* template.tpl (all parameters that need to be substituted need to be prefixed with $)