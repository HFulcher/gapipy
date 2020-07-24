# encoding: utf-8

import click
import gapipy as ga

from .common import cli


@cli.command()
@click.pass_obj
def revoke(scope):
    ga.revoke(**scope.account.credentials.serialize())
