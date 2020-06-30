<!--
https://readme42.com
-->


[![](https://img.shields.io/pypi/v/github-webhooks.svg?maxAge=3600)](https://pypi.org/project/github-webhooks/)
[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/github-webhooks.py/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/github-webhooks.py/actions)

### Installation
```bash
$ [sudo] pip install github-webhooks
```

#### Config
bash|python
-|-
`export GITHUB_TOKEN="your_github_token"`|`os.environ["GITHUB_TOKEN"]="your_github_token"`

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
    <a href="https://readme42.com/">readme42.com</a>
</p>