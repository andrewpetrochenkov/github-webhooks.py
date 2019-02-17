[![](https://img.shields.io/pypi/pyversions/github-webhooks.svg?longCache=True)](https://pypi.org/project/github-webhooks/)
[![](https://img.shields.io/pypi/v/github-webhooks.svg?maxAge=3600)](https://pypi.org/project/github-webhooks/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/github-webhooks.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/github-webhooks.py/)

#### Install
```bash
$ [sudo] pip install github-webhooks
```

#### Config
```bash
$ export GITHUB_TOKEN="xxx"
$ export GITHUB_WEBHOOKS_INI=~/.github-webhooks.ini
```
```python
>>> os.environ["GITHUB_TOKEN"] = "xxx"
```

#### Functions
function|`__doc__`
-|-
`github_webhooks.add(fullname, url, events=['push'])`|add repo webhook
`github_webhooks.delete(fullname, webhooks)`|delete repo webhooks by id or name or url
`github_webhooks.init(fullname, sections)`|init webhook from init file sections
`github_webhooks.api.delete(fullname, hook_id)`|delete repo webhook
`github_webhooks.api.get(fullname)`|return list of repo webhooks data
`github_webhooks.api.request(method, url, data=None, **kwargs)`|make request and return response

#### CLI
usage|`__doc__`
-|-
`python -m github_webhooks.create events url`|create repo webhook(s)
`python -m github_webhooks.delete webhook ...`|delete all repo webhooks
`python -m github_webhooks.init section ...`|init webhook from init file sections
`python -m github_webhooks.names`|print repo webhooks names
`python -m github_webhooks.urls`|print repo webhooks urls

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

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>