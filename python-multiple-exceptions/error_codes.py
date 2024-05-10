import errno
import os
from pprint import pprint

pprint({e: os.strerror(e) for e in sorted(errno.errorcode)})
