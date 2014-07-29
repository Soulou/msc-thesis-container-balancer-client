 # -*- coding: utf-8 -*-

from pprint import pprint
from utils import timestamp_to_time
from prettytable import PrettyTable
from clint.textui import puts, indent, colored
import requests
import json

def nodes_status(self):
    r = requests.get("http://{}:{}/nodes/status".format(self.host, self.port))
    if r.status_code != 200:
        puts(colored.red("Invalid response from server: {} - {}".format(r.status_code, r.text)))
        return

    statuses = json.loads(r.text)
    pprint(statuses)
