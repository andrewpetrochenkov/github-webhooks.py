#!/usr/bin/env python
"""create repo webhook(s)"""
import click
import github_repo
import github_webhooks

MODULE_NAME = "github_webhooks.create"
USAGE = 'python -m %s url ...' % MODULE_NAME
PROG_NAME = 'python -m %s' % MODULE_NAME


@click.command()
@click.argument('urls', nargs=-1, required=True)
def _cli(urls):
    fullname = github_repo.fullname()
    for url in urls:
        github_webhooks.create(fullname, url)


if __name__ == "__main__":
    _cli()
