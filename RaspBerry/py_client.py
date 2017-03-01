import nxppy
import urllib2
import time
from urllib import urlencode

url= "http://10.42.0.1/client.php"

mifare=nxppy.Mifare()
try:
        while True:
                try:
                        uid = mifare.select()
                        print "Read uid", uid

                        params = {'pseudo': uid}
                        http_params = urlencode(params)

                        req= urllib2.Request(url, http_params)
                        connection = urllib2.urlopen(req)

                except nxppy.SelectError:
                        pass
                time.sleep(0.2)
except KeyboardInterrupt:
        pass

