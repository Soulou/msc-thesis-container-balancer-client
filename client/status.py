from utils import timestamp_to_time
from prettytable import PrettyTable
from clint.textui import puts, indent, colored
import requests
import json

def status(self):
    r = requests.get("http://%s:%s/status" % (self.host, self.port))
    if r.status_code != 200:
        puts(colored.red("Invalid response from server: {} - {} ".format(r.status_code, r.text)))
        return

    nodes = json.loads(r.text)

    t = PrettyTable(["Node", "Port", "Service", "Image", "ID", "Created At"])
    t.align["Node"] = "l"
    t.padding_width = 1

    for node, containers in nodes.items():
        for c in containers:
            port = c["Ports"][0]["PublicPort"]
            service = c['Names'][0].split("-")[0][1:]
            id = c["Id"][0:15]
            t.add_row([node, port, service, c["Image"], id, timestamp_to_time(c["Created"])])

    print(t)
