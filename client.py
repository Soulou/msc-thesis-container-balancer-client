#!/usr/bin/env python3

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
@click.argument("container_host", nargs=1)
@click.argument("container_ids", nargs=-1)
def container_status(obj, container_host, container_ids):
    for cid in container_ids:
        obj['client'].container_status(container_host, cid)
    
@client.command()
@click.pass_obj
@click.option("--image", default=None)
@click.argument("service", nargs=1)
def start(obj, service, image):
    obj['client'].start(service, image)

@client.command()
@click.pass_obj
@click.option("--all", default=False, is_flag=True)
@click.option("--service", default=None)
@click.option("--host", default=None)
@click.argument("container_ids", nargs=-1)
def stop(obj, all, service, host, container_ids):
    if service != None:
        obj['client'].stop_service(service)
    if all:
        obj['client'].stop_all(host)
    else:
        obj['client'].stop(host, container_ids)

@client.command()
@click.pass_obj
@click.argument("container_host", nargs=1)
@click.argument("container_ids", nargs=-1)
def migrate(obj, container_host, container_ids):
    obj['client'].migrate(container_host, container_ids)

@client.command()
@click.pass_obj
@click.argument("node", nargs=1)
def node_status(obj, node):
    obj['client'].node_status(node)

@client.command()
@click.pass_obj
@click.argument("strategy", nargs=1, default=None)
@click.option("--opt", default=None, multiple=True)
def balance(obj, strategy, opts):
    obj['client'].balance(strategy, opts)

@client.command()
@click.pass_obj
def nodes_status(obj):
    obj['client'].nodes_status()

if __name__ == '__main__':
    client(obj={})
