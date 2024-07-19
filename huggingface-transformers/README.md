# Hugging Face Transformers: Leverage Open-Source AI in Python

This folder contains the materials for the tutorial [Hugging Face Transformers: Leverage Open-Source AI in Python](https://realpython.com/huggingface-transformers/).

## Installation

Create and activate a virtual environment, and then install the required dependencies:

```sh
(venv) $ python -m pip install transformers torch pillow notebook ipywidgets
```

Alternatively, if you use [Poetry](https://realpython.com/dependency-management-python-poetry/), then you can issue the following command to handle the installation process for you:

```sh
$ poetry install
```

## Usage

Run the sample Python scripts:

```sh
(venv) $ python auto_classes.py
(venv) $ python running_pipelines.py
```

Run the sample Jupyter notebook:

```sh
(venv) $ python -m jupyter notebook gpus_google_colab.ipynb
```

Note that if you run this notebook in Google Colab, then you'll need to update the path to the `requirements.txt` file and the `DATA_PATH` constant accordingly:

```diff
-!pip install -r requirements.txt
+!pip install -r /content/requirements.txt

-DATA_PATH = "Scraped_Car_Review_dodge.csv"
+DATA_PATH = "/content/Scraped_Car_Review_dodge.csv"
```
