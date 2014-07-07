 # -*- coding: utf-8 -*-

from utils import timestamp_to_time
from prettytable import PrettyTable
from clint.textui import puts, indent, colored
import requests
import json

def migrate(self, host, container_ids):
    for id in container_ids:
        r = requests.post("http://{}:{}/container/{}/{}/migrate".format(self.host, self.port, host, id))
        if r.status_code != 201:
            puts(colored.red("Invalid response from server: {} - {}".format(r.status_code, r.text)))
            return

        migration = json.loads(r.text)
        puts("Container {} - {} → {} - {}".format(
            migration['Stopped']['Host'], migration['Stopped']['Id'][0:10],
            migration['Started']['Host'], migration['Started']['Id'][0:10]))
