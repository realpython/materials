import requests
from bs4 import BeautifulSoup
import argparse


def scrape_jobs(location=None):
    """Scrapes Developer job postings from Monster, optionally by location.

    :param location: Where the job is located
    :type location: str
    :return: all job postings from first page that match the search results
    :rtype: BeautifulSoup object
    """
    if location:
        URL = (
            f"https://www.monster.com/jobs/search/"
            f"?q=Software-Developer&where={location}"
        )
    else:
        URL = "https://www.monster.com/jobs/search/?q=Software-Developer"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    return results


def filter_jobs_by_keyword(results, word):
    """Filters job postings by word and prints matching job title plus link.

    :param results: Parsed HTML container with all job listings
    :type results: BeautifulSoup object
    :param word: keyword to filter by
    :type word: str
    :return: None - just meant to print results
    :rtype: None
    """
    filtered_jobs = results.find_all(
        "h2", string=lambda text: word in text.lower()
    )
    for f_job in filtered_jobs:
        link = f_job.find("a")["href"]
        print(f_job.text.strip())
        print(f"Apply here: {link}\n")


def print_all_jobs(results):
    """Print details of all jobs returned by the search.

    The printed details are title, link, company name and location of the job.

    :param results: Parsed HTML container with all job listings
    :type results: BeautifulSoup object
    :return: None - just meant to print results
    :rtype: None
    """
    job_elems = results.find_all("section", class_="card-content")

    for job_elem in job_elems:
        # keep in mind that each job_elem is another BeautifulSoup object!
        title_elem = job_elem.find("h2", class_="title")
        company_elem = job_elem.find("div", class_="company")
        location_elem = job_elem.find("div", class_="location")
        if None in (title_elem, company_elem, location_elem):
            continue
            # print(job_elem.prettify())  # to inspect the 'None' element
        print(title_elem.text.strip())
        link_elem = title_elem.find("a")
        print(link_elem["href"])
        print(company_elem.text.strip())
        print(location_elem.text.strip())
        print()


# USE THE SCRIPT AS A COMMAND-LINE INTERFACE
# ----------------------------------------------------------------------------
my_parser = argparse.ArgumentParser(
    prog="jobs", description="Find Developer Jobs"
)
my_parser.add_argument(
    "-location", metavar="location", type=str, help="The location of the job"
)
my_parser.add_argument(
    "-word", metavar="word", type=str, help="What keyword to filter by"
)

args = my_parser.parse_args()
location, keyword = args.location, args.word

results = scrape_jobs(location)
if keyword:
    filter_jobs_by_keyword(results, keyword.lower())
else:
    print_all_jobs(results)
