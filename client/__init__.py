from .client import *
from .status import *
from .start import *
from .stop import *
from .migrate import *
from .node_status import *
from .nodes_status import *
from .container_status import *
from .balance import *

Client.start = start
Client.stop = stop
Client.stop_service = stop_service
Client.stop_all = stop_all
Client.status = status
Client.migrate = migrate
Client.node_status = node_status
Client.nodes_status = nodes_status
Client.container_status = container_status
Client.balance = balance
