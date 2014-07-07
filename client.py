#!/usr/bin/env python

from clint.textui import puts, indent, colored
import click

from client import Client

agent_client = None

@click.group()
@click.option('--host', default='localhost')
@click.option('--port', default=5001)
@click.pass_obj
def client(obj, host, port):
    obj['client'] = Client(host, port)

@client.command()
@click.pass_obj
def status(obj):
    obj['client'].status()
    
@client.command()
@click.pass_obj
@click.argument("service", nargs=1)
def start(obj, service):
    obj['client'].start(service)

@client.command()
@click.pass_obj
@click.option("--all", default=False, is_flag=True)
@click.argument("container_host", nargs=1)
@click.argument("container_ids", nargs=-1)
def stop(obj, all, container_host, container_ids):
    if all:
        obj['client'].stop_all(container_host)
    else:
        obj['client'].stop(container_host, container_ids)

@client.command()
@click.pass_obj
@click.argument("container_host", nargs=1)
@click.argument("container_ids", nargs=-1)
def migrate(obj, container_host, container_ids):
    obj['client'].migrate(container_host, container_ids)

if __name__ == '__main__':
    client(obj={})
