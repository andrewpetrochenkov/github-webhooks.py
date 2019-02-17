#!/usr/bin/env python
"""create repo webhook(s)"""
import click
import github_repo
import github_webhooks

MODULE_NAME = "github_webhooks.create"
USAGE = 'python -m %s events url' % MODULE_NAME
PROG_NAME = 'python -m %s' % MODULE_NAME


@click.command()
@click.argument('events', required=True)
@click.argument('url', required=True)
def _cli(events, url):
    fullname = github_repo.fullname()
    events = events.replace(" ","").split(",")
    for url in urls:
        github_webhooks.create(fullname, url, events)


if __name__ == "__main__":
    _cli()
