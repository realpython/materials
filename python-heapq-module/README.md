# Finding the Shortest Path on a Map

Code supplementing the [Using the Python "heapq" Module and Priority Queues](https://realpython.com/python-heapq-module/) article.

## Usage

Run the following program:

```shell
$ python shortest-path.py
```

It will print out a map with the shortest path from the top-left corner to the bottom-right corner indicated with `@`.

## Changing the Map

In order to change the map the robot uses, modify the triple-quoted string that is assigned to `map` near the top of the file. Anything except `X` is interpreted as free from obstacles. Using `.` makes the map easier to read directly. You can make the map bigger, and a lot more complicated.

If there are so many obstacles that make finding a path from the top-left corner to the bottom right corner impossible, the program will raise an exception.

## Changing the Rules

If you want to play around with the code, here are some changes that you can make:

* How would you change the code so that the robot cannot go diagonally?
* How would you change the code so that the robot can only move right or down, but never left or up?
* (Harder) How would you change the code so that every step consumes energy, squares with `*` give energy, and the robot cannot move if it is out of energy?
* (Challenge) How would you change the code so that areas marked with `#` are not obstacles, but take twice as long to move through?
