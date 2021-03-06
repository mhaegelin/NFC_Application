import requests
from bs4 import BeautifulSoup

url= "http://109.15.75.65/Appli/trace"

uid = "373,427,142,451,500,126,869,500" #4EB55F96 Davy -- AED16796 Marco

client = requests.session()
# Retrieve the CSRF token
soup = BeautifulSoup(client.get(url).content, "lxml")
csrftoken = soup.find('input', {"name": "csrfmiddlewaretoken"}).get("value")
# Create the params
params = dict(traceNFC=uid, csrfmiddlewaretoken=csrftoken)
r = client.post(url, data=params, headers=dict(Referer=url))
