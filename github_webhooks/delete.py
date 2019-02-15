#!/usr/bin/env python
"""delete all repo webhooks"""
import click
import github_repo
import github_webhooks

MODULE_NAME = "github_webhooks.delete"
USAGE = 'python -m %s' % MODULE_NAME
PROG_NAME = 'python -m %s' % USAGE


@click.command()
def _cli():
    fullname = github_repo.fullname()
    github_webhooks.delete(fullname)


if __name__ == "__main__":
    _cli()
