# Code Repository for Web Scraping Course

This repository contains Jupyter Notebooks with code examples relating to the Real Python video course on [Building a Web Scraper with `requests` and Beautiful Soup](https://realpython.com/courses/web-scraping-beautiful-soup/).

## Setup

Create and activate a virtual environment, then install `requests`, `beautifulsoup4`, and `jupyter`:

```bash
$ python -m venv venv
$ source venv/bin/activate
# PS> venv\Scripts\activate  # on Windows
(venv) $ python -m pip install -r requirements.txt
```

Once all the dependencies are installed, you can start the Jupyter notebook server:

```bash
(venv) $ jupyter notebook
```

Now you can open the notebook that you want to work on.

## Notebook Files

The notebooks 01--03 represent the **web scraping pipeline** discussed in the course:

- **Part 1: Inspect** `01_inspect.ipynb`
- **Part 2: Scrape** `02_scrape.ipynb`
- **Part 3: Parse** `03_parse.ipynb`

The notebook 04 contains tasks to work on individually so you can keep practicing the discussed concepts and personalize the project for yourself:

- **Tasks** `04_pipeline.ipynb`

Attempt to build out your individual pipeline by yourself. When you're done with the suggested practice website, try to repeat the process with a different website. All the best, and keep learning! :)

## ⚠️ Durabilty Warning ⚠️

Like [mentioned in the course](https://realpython.com/lessons/challenge-of-durability/), websites frequently change. Unfortunately the job board that you'll see in the course, indeed.com, has started to block scraping of their site since the recording of the course.

Just like in the associated written tutorial on [web scraping with beautiful soup](https://realpython.com/beautiful-soup-web-scraper-python/#scrape-the-fake-python-job-site), you can instead use [Real Python's fake jobs site](https://realpython.github.io/fake-jobs/) to practice scraping a static website.

All the concepts discussed in the course lessons are still accurate. Translating what you see onto a different website will be a good learning opportunity where you'll have to synthesize the information and apply it practically.

## About the Author

Martin Breuss - Email: martin@realpython.com

## License

Distributed under the MIT license. See `LICENSE` in the root directory of this `materials` repo for more information.
