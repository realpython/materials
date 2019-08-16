"""Companion code to https://realpython.com/simulation-with-simpy/

'Simulating Real-World Processes With SimPy'

Python version: 3.7.3
SimPy version: 3.0.11
"""

import simpy
import random


class Theater(object):
    def __init__(self, env, num_cashiers, num_servers, num_ushers):
        self.env = env
        self.cashier = simpy.Resource(env, num_cashiers)
        self.server = simpy.Resource(env, num_servers)
        self.usher = simpy.Resource(env, num_ushers)

    def purchase_ticket(self, moviegoer):
        yield self.env.timeout(random.randint(1, 2))

    def sell_food(self, moviegoer):
        yield self.env.timeout(random.randint(0, 5))

    def check_ticket(self, moviegoer):
        yield self.env.timeout(3 / 60)


def moviegoer(env, num, theater):
    with theater.cashier.request() as request:
        yield request
        yield env.process(theater.purchase_ticket(num))

    with theater.server.request() as request:
        yield request
        yield env.process(theater.sell_food(num))

    with theater.usher.request() as request:
        yield request
        yield env.process(theater.check_ticket(num))

    departure_time = env.now
    departure_times.append(departure_time)


def run_theater(env, num_cashiers, num_servers, num_ushers):
    theater = Theater(env, num_cashiers, num_servers, num_ushers)
    interarrival = 0.20

    for num in range(3):
        env.process(moviegoer(env, num, theater))
        arrival_time = env.now
        arrival_times.append(arrival_time)

    while True:
        # Wait a bit before generating a new person
        yield env.timeout(interarrival)

        num += 1
        env.process(moviegoer(env, num, theater))  # Generate the next person
        arrival_time = env.now
        arrival_times.append(arrival_time)


def calculate_wait_time(arrival_times, departure_times):
    total_wait = []
    num_cleared = len(departure_times)

    for i in range(num_cleared):
        total_wait.append(departure_times[i] - arrival_times[i])

    # Pretty print the results
    average_wait = sum(total_wait) / num_cleared
    minutes, frac_minutes = divmod(average_wait, 1)
    seconds = frac_minutes * 60
    return round(minutes), round(seconds)


def get_user_input():
    num_cashiers = input("Input # of cashiers working: ")
    num_servers = input("Input # of servers working: ")
    num_ushers = input("Input # of ushers working: ")
    params = [num_cashiers, num_servers, num_ushers]
    if all(str(i).isdigit() for i in params):  # Check input is valid
        params = [int(x) for x in params]
    else:
        print(
            "Could not parse input. The simulation will use default values:",
            "\n1 cashier, 1 server, 1 usher.",
        )
        params = [1, 1, 1]
    return params


def main():
    # Setup
    random.seed(42)
    num_cashiers, num_servers, num_ushers = get_user_input()

    # Run the simulation
    env = simpy.Environment()
    env.process(run_theater(env, num_cashiers, num_servers, num_ushers))
    env.run(until=90)

    # View the results
    mins, secs = calculate_wait_time(arrival_times, departure_times)
    print(
        "Running simulation...",
        f"\nThe average wait time is {mins} minutes and {secs} seconds.",
    )


if __name__ == "__main__":
    arrival_times = []
    departure_times = []
    main()
