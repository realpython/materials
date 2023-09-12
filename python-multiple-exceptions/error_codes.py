import os
import errno
from pprint import pprint

pprint({e: os.strerror(e) for e in sorted(errno.errorcode)})
