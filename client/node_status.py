 # -*- coding: utf-8 -*-

from pprint import pprint
from utils import timestamp_to_time
from prettytable import PrettyTable
from clint.textui import puts, indent, colored
import requests
import json

def node_status(self, node):
    r = requests.get("http://{}:{}/node/{}/status".format(self.host, self.port, node))
    if r.status_code != 200:
        puts(colored.red("Invalid response from server: {} - {}".format(r.status_code, r.text)))
        return

    status = json.loads(r.text)
    pprint(status)
