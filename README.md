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
```
```python
>>> os.environ["GITHUB_TOKEN"] = "xxx"
```

#### Functions
function|`__doc__`
-|-
`github_webhooks.create(fullname, url, events=['push'])`|create repo webhook
`github_webhooks.delete(fullname)`|delete all repo webhooks
`github_webhooks.get(fullname)`|return list of repo webhooks data
`github_webhooks.urls(fullname)`|return list of repo webhooks urls

#### CLI
usage|`__doc__`
-|-
`python -m github_webhooks.create url ...`|create repo webhook(s)
`python -m github_webhooks.delete`|delete all repo webhooks
`python -m github_webhooks.urls`|print repo webhooks urls

#### Links
+   [webhooks REST API v3](https://developer.github.com/v3/repos/hooks/)

<p align="center"><a href="https://pypi.org/project/readme-md/">readme-md</a> - README.md generator</p>