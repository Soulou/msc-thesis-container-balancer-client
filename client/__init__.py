from .client import *
from .status import *
from .start import *
from .stop import *
from .migrate import *

Client.start = start
Client.stop = stop
Client.stop_all = stop_all
Client.status = status
Client.migrate = migrate
