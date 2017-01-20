import nxppy
import urllib2
import time
from urllib import urlencode

url= "http://10.42.0.1/client.php"
temps=0
ancien_uid= "petitTasDeMerde"
mifare=nxppy.Mifare()
try:
	while True:
		try:
			uid= mifare.select()
        		if (uid != ancien_uid) or ((time.time() - temps) >3):
				ancien_uid= uid
				temps= time.time()
				#print "Read uid", uid
				params = {'pseudo': uid}
				http_params = urlencode(params)

				req= urllib2.Request(url, http_params)
				connection = urllib2.urlopen(req)

		except nxppy.SelectError:
        		pass
	 	time.sleep(0.2)   
except KeyboardInterrupt:
        pass
