import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor

teller_barrier = threading.Barrier(3)


def prepare_for_work(name):
    print(f"{int(time.time())}: {name} is preparing their counter.")

    # Simulate the delay to prepare the counter
    time.sleep(random.randint(1, 3))
    print(f"{int(time.time())}: {name} has finished preparing.")

    # Wait for all tellers to finish preparing
    teller_barrier.wait()
    print(f"{int(time.time())}: {name} is now ready to serve customers.")


tellers = ["Teller 1", "Teller 2", "Teller 3"]

with ThreadPoolExecutor(max_workers=3) as executor:
    for teller_name in tellers:
        executor.submit(prepare_for_work, teller_name)

print(f"{int(time.time())}: All tellers are ready to serve customers.")
