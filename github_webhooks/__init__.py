#!/usr/bin/env python
import ini2dict
import json
import os
import public
import requests
import github_webhooks.api


GITHUB_WEBHOOKS_INI = os.path.expanduser("~/.github-webhooks.ini")
GITHUB_WEBHOOKS_INI = os.getenv("GITHUB_WEBOOKS_INI",GITHUB_WEBHOOKS_INI)

@public.add
def add(fullname, url, events=["push"]):
    """add repo webhook"""
    if not events:
        events = ["push"]
    api_url = "https://api.github.com/repos/%s/hooks" % fullname
    config = dict(url=url, content_type="json")
    data = dict(name="web", active=True, events=events, config=config)
    return request("POST", api_url, data).json()


@public.add
def delete(fullname, webhooks):
    """delete repo webhooks by id or name or url"""
    data = get(fullname)
    for hook in data:
        hook_id = hook["id"]
        name = hook["name"]
        url = hook["config"]["url"]
        if hook == hook_id or hook == name or hook == url:
            github_webhooks.api.delete(fullname,hook_id)

@public.add
def init(fullname, sections):
    """init webhook from init file sections"""
    webhooks = ini2dict.read(GITHUB_WEBHOOKS_INI)
    for section in sections:
        webhooks[section]
        url = webhooks[section]["url"]
        events = webhooks[section].get("events","push")
        add(fullname, url, events=events)
