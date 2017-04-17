import nxppy
import time
import requests
from bs4 import BeautifulSoup

url= "http://127.0.0.1:8000/Appli/trace"

mifare=nxppy.Mifare()
try:
        while True:
                try:
                        uid = mifare.select()
                        print "Read uid", uid

                        client = requests.session()
						# Retrieve the CSRF token
                        soup = BeautifulSoup(client.get(url).content, "lxml")
                        csrftoken = soup.find('input', {"name": "csrfmiddlewaretoken"}).get("value")
                        # Create the params
                        params = dict(traceNFC=uid, csrfmiddlewaretoken=csrftoken)
                        r = client.post(url, data=params, headers=dict(Referer=url))

                except nxppy.SelectError:
                        pass
                time.sleep(0.2)
except KeyboardInterrupt:
        pass

