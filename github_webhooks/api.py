__all__ = ['request', 'get', 'delete']


import json
import os
import requests

"""
https://developer.github.com/v3/repos/hooks/
"""


def request(method, url, data=None, **kwargs):
    """make request and return response"""
    token = os.environ["GITHUB_TOKEN"]
    if "headers" not in kwargs:
        kwargs["headers"] = {}
    kwargs["headers"].update({"Authorization": "Bearer %s" % token})
    if data is not None:
        data = json.dumps(data)
    r = requests.request(method, url, data=data, **kwargs)
    r.raise_for_status()
    return r


def get(fullname):
    """return a list of repo webhooks data"""
    url = "https://api.github.com/repos/%s/hooks" % fullname
    return request("GET", url).json()


def delete(fullname, hook_id):
    """delete repo webhook"""
    url = "https://api.github.com/repos/%s/hooks/%s" % (fullname, int(hook_id))
    request("DELETE", url)
