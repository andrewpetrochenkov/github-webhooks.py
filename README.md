<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/github-webhooks.svg?longCache=True)](https://pypi.org/project/github-webhooks/)
[![](https://img.shields.io/pypi/v/github-webhooks.svg?maxAge=3600)](https://pypi.org/project/github-webhooks/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/github-webhooks.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/github-webhooks.py/)

#### Installation
```bash
$ [sudo] pip install github-webhooks
```

#### Config
bash|python
-|-
`export GITHUB_TOKEN="your_github_token"`|`os.environ["GITHUB_TOKEN"]="your_github_token"`

#### Functions
function|`__doc__`
-|-
`github_webhooks.exists(fullname, webhook)` |return True if webhook exists
`github_webhooks.api.delete(fullname, hook_id)` |delete repo webhook
`github_webhooks.api.get(fullname)` |return a list of repo webhooks data
`github_webhooks.api.request(method, url, data=None, **kwargs)` |make request and return response

#### Executable modules
usage|`__doc__`
-|-
`python -m github_webhooks.add events url` |add repo webhook(s)
`python -m github_webhooks.delete webhook ...` |delete all repo webhooks
`python -m github_webhooks.init section ...` |init webhook from init file sections
`python -m github_webhooks.names` |print repo webhooks names
`python -m github_webhooks.urls` |print repo webhooks urls

#### Examples
```bash
$ cd path/to/repo
$ python -m github_webhooks.create "push" https://xxx.execute-api.us-east-1.amazonaws.com/run
$ python -m github_webhooks.names
web
$ python -m github_webhooks.urls
https://xxx.execute-api.us-east-1.amazonaws.com/run
$ python -m github_webhooks.delete "web"
```

`~/.github-webhooks.ini`
```
[name]
  url = https://xxx.execute-api.us-east-1.amazonaws.com/run
  events = push
```

```
$ python -m github_webhooks.init "name"
```

#### Links
+   [webhooks REST API v3](https://developer.github.com/v3/repos/hooks/)

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>