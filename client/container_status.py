 # -*- coding: utf-8 -*-

from pprint import pprint
from utils import timestamp_to_time
from clint.textui import puts, indent, colored
import requests
import json

def container_status(self, host, cid):
    r = requests.get("http://{}:{}/node/{}/{}/status".format(self.host, self.port, host, cid))
    if r.status_code != 200:
        puts(colored.red("Invalid response from server: {} - {}".format(r.status_code, r.text)))
        return

    puts(colored.blue("{} - {}\n".format(host, cid)))

    status = json.loads(r.text)
    pprint(status)
