# Digitar

A digital guitar and a tablature player.

## Installation

Install the project along with its dependencies into a virtual environment managed by Poetry:

```sh
$ poetry install
```

## Usage

Activate the project's virtual environment: 

```sh
$ poetry shell
```

Change directory to the `demo/` subfolder and run the sample scripts:

```sh
(digitar-py3.12) $ cd demo/
(digitar-py3.12) $ python play_chorus.py
(digitar-py3.12) $ python play_diablo.py
```

Read the tablature from the custom YAML file format:

```sh
$ play-tab tabs/doom.yaml 
Saved file /home/user/digital-guitar/demo/doom.mp3

$ play-tab tabs/foggy-mountain-breakdown.yaml -o foggy.mp3
Saved file /home/user/digital-guitar/demo/foggy.mp3
```
