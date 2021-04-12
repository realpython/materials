import requests
from bs4 import BeautifulSoup


URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ResultsContainer")

# Look for Python jobs
print("PYTHON JOBS\n==============================\n")
python_jobs = results.find_all("h2", string=lambda text: "python" in text.lower())
python_job_elems = [title_elem.parent.parent.parent for title_elem in python_jobs]
for p_job in python_job_elems:
    title_elem = p_job.find("h2", class_="title")
    link_url = p_job.find_all("a")[1]["href"]
    print(title_elem.text.strip())
    print(f"Apply here: {link_url}\n")

# Print out all available jobs from the scraped webpage
print("ALL JOBS\n==============================\n")
job_elems = results.find_all("div", class_="card-content")
for job_elem in job_elems:
    title_elem = job_elem.find("h2", class_="title")
    company_elem = job_elem.find("h3", class_="company")
    location_elem = job_elem.find("p", class_="location")
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()
