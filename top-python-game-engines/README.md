# Top Python Game Engines

This repository contains source code for sample games you'll see in Real Python's Top Python Game Engines article.

After cloning this repository, you can navigate into each folder to find the source code for the sample games shown in the article. Instructions on how to run each game is shown below.

## Setup the Virtual Environment

It is recommended to use a virtual environment to run these samples. To do so, follow these instructions.

First, create the virtual environment:

```bash
$ python3 -m venv venv
```

Next, activate the virtual environment:

```bash
$ source ./venv/bin/activate
```

Finally, install the dependencies for these projects:

```bash
(venv) $ python -m pip install -r requirements.txt
```

## Pygame

To run the Pygame sample code, first activate the virtual environment:

```bash
$ source ./venv/bin/activate
```

Then navigate to the Pygame folder:

```bash
(venv) $ cd pygame
```

To run the basic game:

```bash
(venv) $ python pygame_basic.py
```

To run the full sample game:

```bash
(venv) $ python pygame_game.py
```

## Pygame Zero

To run the Pygame Zero sample code, first activate the virtual environment:

```bash
$ source ./venv/bin/activate
```

Then navigate to the Pygame folder:

```bash
(venv) $ cd pygame_zero
```

To run the basic game:

```bash
(venv) $ python pygame_zero_basic.py
```

To run the full sample game:

```bash
(venv) $ python pygame_zero_game.py
```

Alternately, you can use `pgzrun` to run both games:

```bash
(venv) $ pgzrun pygame_zero_game.py
```

## Arcade

To run the Arcade sample code, first activate the virtual environment:

```bash
$ source ./venv/bin/activate
```

Then navigate to the Arcade folder:

```bash
(venv) $ cd arcade
```

To run the basic game:

```bash
(venv) $ python arcade_basic.py
```

To run the full sample game:

```bash
(venv) $ python arcade_game.py
```

## AdventureLib

To run the AdventureLib sample code, first activate the virtual environment:

```bash
$ source ./venv/bin/activate
```

Then navigate to the AdventureLib folder:

```bash
(venv) $ cd adventurelib
```

To run the basic game:

```bash
(venv) $ python adventurelib_basic.py
```

To run the full sample game:

```bash
(venv) $ python adventurelib_game.py
```
## Ren'Py

Unlike the other samples, Ren'Py games are developed and run from the Ren'Py Software Development Kit.

Visit the [Ren'Py web page](https://www.renpy.org/) to download the proper SDK for your environment (Windows, Mac, and Linux versions are available).

Then, run the Ren'Py Launcher using the proper command for your environment. Check out the [Ren'Py Quickstart Guide](https://www.renpy.org/doc/html/quickstart.html#the-ren-py-launcher) for the most up to date instructions.

To access the basic and full sample games in the Ren'Py launcher, click _Preferences_, then _Projects Directory_. Change the Projects Directory to the `renpy` folder in the repository folder you downloaded. Click _Return_ to return to the main Ren'Py Launcher page.

To run the basic game, click on `basic_game` in the Projects list on the left, then click _Launch Project_.
To run the full sample game, click on `giant_quest_game` in the Projects list on the left, then click _Launch Project_.

