 # -*- coding: utf-8 -*-

from pprint import pprint
from utils import timestamp_to_time
from prettytable import PrettyTable
from clint.textui import puts, indent, colored
import requests
import json

def start(self, service, image=None):
    payload = {"service": service}
    if image != None: 
        payload["image"] = image

    r = requests.post("http://%s:%s/containers" % (self.host, self.port), data=payload)
    if r.status_code != 201:
        puts(colored.red("Invalid response from server: {} - {}".format(r.status_code, r.text)))
        return

    container = json.loads(r.text)
    puts("Container created")
    with indent(4):
        puts("→ Host: {}".format(container["Host"]))
        puts("→ ID: {}".format(container["Id"]))
        puts("→ Service: {}".format(service))
        puts("→ Image: {}".format(container['Config']['Image']))

        port_bindings = container["NetworkSettings"]["Ports"]
        for remote_port, bindings in port_bindings.items():
            port = bindings[0]["HostPort"]
            break
        puts("→ Port: {}".format(port))
