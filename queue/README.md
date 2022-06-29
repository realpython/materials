# Python Stacks, Queues, and Priority Queues in Practice

Sample code supplementing the tutorial on [Python queues](https://realpython.com/queue-in-python/) hosted on Real Python.

## Installation

To get started, create and activate a new virtual environment, and then install the required dependencies into it:

```shell
$ python3 -m venv venv/ --prompt=queue
$ source venv/bin/activate
(queue) $ python -m pip install -r requirements.txt -c constraints.txt
```

## Usage

### Queue Implementation

Change directory to `src/` and run the interactive Python interpreter:

```shell
(queue) $ cd src/
(queue) $ python -q
```

Then, import various queue data types from the `queues` module and start using them:

```python
>>> from queues import Queue, Stack, PriorityQueue

>>> fifo, stack, heap = Queue(), Stack(), PriorityQueue()
>>> for priority, element in enumerate(["1st", "2nd", "3rd"]):
...     fifo.enqueue(element)
...     stack.enqueue(element)
...     heap.enqueue_with_priority(priority, element)

>>> for elements in zip(fifo, stack, heap):
...     print(elements)
...
('1st', '3rd', '3rd')
('2nd', '2nd', '2nd')
('3rd', '1st', '1st')
```

### Graph Algorithms

Change directory to `src/` and run the interactive Python interpreter:

```shell
(queue) $ cd src/
(queue) $ python -q
```

Then, import various `graph` module members and start using them:

```python
>>> from graph import *

>>> nodes, graph = load_graph("roadmap.dot", City.from_dict)

>>> city1 = nodes["london"]
>>> city2 = nodes["edinburgh"]
 
>>> def distance(weights):
...     return float(weights["distance"])

>>> for city in dijkstra_shortest_path(graph, city1, city2, distance):
...     print(city.name)
...
City of London
St Albans
Coventry
Birmingham
Stoke-on-Trent
Manchester
Salford
Preston
Lancaster
Carlisle
Edinburgh

>>> for city in shortest_path(graph, city1, city2):
...     print(city.name)
...
City of London
Bristol
Newport
St Asaph
Liverpool
Preston
Lancaster
Carlisle
Edinburgh

>>> connected(graph, city1, city2)
True

>>> def is_twentieth_century(city):
...     return city.year and 1901 <= city.year <= 2000

>>> breadth_first_search(graph, city2, is_twentieth_century)
City(
    name='Lancaster',
    country='England',
    year=1937,
    latitude=54.047,
    longitude=-2.801
)

>>> depth_first_search(graph, city2, is_twentieth_century)
City(
    name='Lancaster',
    country='England',
    year=1937,
    latitude=54.047,
    longitude=-2.801
)
```

### Thread-Safe Queues

Change directory to `src/` and run the script with optional parameters. For example:

```shell
(queue) $ cd src/
(queue) $ python thread_safe_queues.py --queue fifo \
                                       --producers 3 \
                                       --consumers 2 \
                                       --producer-speed 1 \
                                       --consumer-speed 1
```

**Parameters:**

| Short Name |          Long Name | Value                  |
|-----------:|-------------------:|------------------------|
|       `-q` |          `--queue` | `fifo`, `lifo`, `heap` |
|       `-p` |      `--producers` | number                 |
|       `-c` |      `--consumers` | number                 |
|      `-ps` | `--producer-speed` | number                 |
|      `-cs` | `--consumer-speed` | number                 |

### Asynchronous Queues

Change directory to `src/` and run the script with a mandatory URL and optional parameters:

```shell
(queue) $ cd src/
(queue) $ python async_queues.py http://localhost:8000/ --max-depth 2 \
                                                        --num-workers 3
```

**Parameters:**

| Short Name |       Long Name | Value  |
|-----------:|----------------:|--------|
|       `-d` |   `--max-depth` | number |
|       `-w` | `--num-workers` | number |

Note that to change between the available queue types, you'll need to edit your `main()` coroutine function:

```python
# async_queues.py

# ...

async def main(args):
    session = aiohttp.ClientSession()
    try:
        links = Counter()
        queue = asyncio.Queue()
        # queue = asyncio.LifoQueue()
        # queue = asyncio.PriorityQueue()

# ...
```

### Multiprocessing Queue

Change directory to `src/` and run the script with a mandatory MD5 hash value and optional parameters:

```shell
(queue) $ cd src/
(queue) $ python async_queues.py a9d1cbf71942327e98b40cf5ef38a960 -m 6 -w 4
```

**Parameters:**

| Short Name |       Long Name | Value  |
|-----------:|----------------:|--------|
|       `-m` |  `--max-length` | number |
|       `-w` | `--num-workers` | number |

The maximum length determines the maximum number of characters in a text to guess. If you skip the number of workers, then the script will create as many of them as the number of CPU cores detected.

### Message Brokers

#### RabbitMQ

Start a RabbitMQ broker with Docker:

```shell
$ docker run -it --rm --name rabbitmq -p 5672:5672 rabbitmq
```

Open separate terminal windows, activate your virtual environment, change directory to `message_brokers/rabbitmq/`, and run your producer and consumer scripts:  

```shell
(queue) $ cd message_brokers/rabbitmq/
(queue) $ python producer.py
(queue) $ python consumer.py
```

You can have as many producers and consumers as you like.

#### Redis

Start a Redis server with Docker:

```shell
$ docker run -it --rm --name redis -p 6379:6379 redis
```

Open separate terminal windows, activate your virtual environment, change directory to `message_brokers/redis/`, and run your publisher and subscriber scripts:  

```shell
(queue) $ cd message_brokers/redis/
(queue) $ python publisher.py
(queue) $ python subscriber.py
```

You can have as many publishers and subscribers as you like.

#### Apache Kafka

Change directory to `message_brokers/kafka/` and start an Apache Kafka cluster with Docker Compose:

```shell
$ cd message_brokers/kafka/
$ docker-compose up
```

Open separate terminal windows, activate your virtual environment, change directory to `message_brokers/kafka/`, and run your producer and consumer scripts:  

```shell
(queue) $ cd message_brokers/kafka/
(queue) $ python producer.py
(queue) $ python consumer.py
```

You can have as many producers and consumers as you like.
