import os
import threading

import fibmodule

for _ in range(os.cpu_count()):
    threading.Thread(target=fibmodule.fib, args=(45,)).start()
