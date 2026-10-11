import pandas as pd
import requests
from bs4 import BeautifulSoup
# pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

url=r"https://www.python.org/jobs/"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
if response.status_code != 200:
    print("URL not found")
    exit()
# print(response.text)
soup=BeautifulSoup(response.text,"html.parser") #find tags, extract text
# print(soup.prettify())

jobs_container=soup.find("ol",class_="list-recent-jobs list-row-container menu")
# print(jobs_container.prettify())

if not jobs_container:
    print("Jobs container not found")
    exit()

jobs = jobs_container.find_all("li")
# print(jobs)
job=[]
for li in jobs:
    title_tag=li.find("a")
    company_tag=li.find("span",class_="listing-company-name")
    location_tag=li.find("span",class_="listing-location")
    date_tag=li.find('time')



    jobs={
        "Job Title": title_tag.get_text(strip=True) if title_tag else None,
        "Company_name": company_tag.contents[-1].strip() if company_tag else None,
        "Location": location_tag.get_text(strip=True) if location_tag else None,
        "Posted Date": date_tag.get_text(strip=True) if date_tag else None,
    }

    job.append(jobs)

# print(job)

df=pd.DataFrame(job)

df.to_csv("jobs.csv",index=False)
print("completed successfully")