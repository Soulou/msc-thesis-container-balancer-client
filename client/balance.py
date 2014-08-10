 # -*- coding: utf-8 -*-

from pprint import pprint
from utils import timestamp_to_time
from prettytable import PrettyTable
from clint.textui import puts, indent, colored
import requests
import json

def start(self, strategy):
    payload = {}
    if strategy != None: 
        payload["strategy"] = strategy

    r = requests.post("http://%s:%s/balance" % (self.host, self.port), data=payload)
    if r.status_code != 200:
        puts(colored.red("Invalid response from server: {} - {}".format(r.status_code, r.text)))
        return

    result = json.loads(r.text)
    pprint(result)