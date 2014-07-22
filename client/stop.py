from utils import timestamp_to_time
from prettytable import PrettyTable
from clint.textui import puts, indent, colored
import requests
import json

def stop(self, host, container_ids):
    for id in container_ids:
        r = requests.delete("http://{}:{}/container/{}/{}".format(self.host, self.port, host, id))
        if r.status_code != 204:
            puts(colored.red("Invalid response from server: {} - {}".format(r.status_code, r.text)))
            return

        puts("Container {} from {} has been stopped".format(id, host))

def stop_service(self, service):
    r = requests.get("http://{}:{}/status".format(self.host, self.port))
    if r.status_code != 200:
        puts(colored.red("Invalid response from server: {} - {} ".format(r.status_code, r.text)))
        return

    containers = json.loads(r.text)
    for host, containers in containers.iteritems():
        service_containers = []
        for c in containers:
            if c['Names'][0].split("-")[0][1:] == service:
                service_containers.append(c)

        self.stop(host, map((lambda container: container["Id"]), service_containers))


def stop_all(self, host):
    r = requests.get("http://{}:{}/node/{}/containers".format(self.host, self.port, host))
    if r.status_code != 200:
        puts(colored.red("Invalid response from server: {} - {} ".format(r.status_code, r.text)))
        return

    containers = json.loads(r.text)
    self.stop(host, map((lambda container: container["Id"]), containers))
