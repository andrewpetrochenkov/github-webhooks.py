__all__ = ['add', 'delete', 'exists']


import os
import values
import github_webhooks.api


def exists(fullname, webhook):
    """return True if webhook exists"""
    for hook in github_webhooks.api.get(fullname):
        name = hook["name"]
        url = hook["config"]["url"]
        if hook == name or hook == url:
            return True
    return False


def add(fullname, url, events=["push"]):
    """add repo webhook"""
    if not events:
        events = ["push"]
    for hook in github_webhooks.api.get(fullname):
        if hook["config"]["url"] == url:
            return hook
    events = values.get(events)
    api_url = "https://api.github.com/repos/%s/hooks" % fullname
    config = dict(url=url, content_type="json")
    data = dict(name="web", active=True, events=events, config=config)
    return github_webhooks.api.request("POST", api_url, data).json()


def delete(fullname, webhooks):
    """delete repo webhooks by id or name or url"""
    data = github_webhooks.api.get(fullname)
    for webhook in values.get(webhooks):
        for hook in data:
            hook_id = hook["id"]
            name = hook["name"]
            url = hook["config"]["url"]
            if webhook == hook_id or webhook == name or webhook == url:
                github_webhooks.api.delete(fullname, hook_id)
