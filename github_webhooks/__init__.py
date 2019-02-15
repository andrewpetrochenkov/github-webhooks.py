#!/usr/bin/env python
import json
import os
import public
import requests

"""
https://developer.github.com/webhooks/
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


@public.add
def get(fullname):
    """return list of repo webhooks data"""
    api_url = "https://api.github.com/repos/%s/hooks" % fullname
    return request("GET", api_url).json()


@public.add
def names(fullname):
    """return list of webhooks names"""
    return list(map(lambda h: h["name"], get(fullname)))


@public.add
def create(fullname, url, events=["push"]):
    """create repo webhook"""
    if not events:
        events = ["push"]
    api_url = "https://api.github.com/repos/%s/hooks" % fullname
    config = dict(url=url, content_type="json")
    data = dict(name="web", active=True, events=events, config=config)
    return request("POST", api_url, data).json()


@public.add
def urls(fullname):
    """return list of repo webhooks urls"""
    result = []
    for hook in get(fullname):
        url = hook["config"]["url"]
        result.append(url)
    return result


def hook_id(url):
    for hook in get():
        if hook["config"]["url"] == url:
            return hook["id"]


@public.add
def delete(fullname, webhooks):
    """delete repo webhooks by name or url"""
    data = get(fullname)
    for hook in data:
        hook_id = hook["id"]
        name = hook["name"]
        url = hook["config"]["url"]
        api_url = "https://api.github.com/repos/%s/hooks/%s" % (fullname, hook_id)
        if name in webhooks or url in webhooks:
            request("DELETE", api_url)
