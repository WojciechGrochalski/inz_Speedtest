import os
import time
import speedtest
import json

try:
    interval = int(os.environ['interval'])
except:
    interval = 5


def st():
    downloads = 0.00
    upload = 0.00
    try:
        speed_test = speedtest.Speedtest()
        speed_test.get_best_server()
        res = speed_test.get_best_server()

        print('0) Server location: ', end='')
        print(res["name"])
        data = {"downloads": downloads, "uploads": upload, "ping": int(speed_test.results.ping), "serverLocation": res["name"]}
        with open('/var/www/localhost/htdocs/data.json', 'w') as outfile:
            json.dump(data, outfile)

        print('1) Download Speed: ', end='')
        downloads = round(speed_test.download() / 1000000, 1)
        print(downloads, "Mbps")
        data = {"downloads": downloads, "uploads": upload, "ping": int(speed_test.results.ping), "serverLocation": res["name"]}
        with open('/var/www/localhost/htdocs/data.json', 'w') as outfile:
            json.dump(data, outfile)

        print('1) Upload Speed: ', end='')
        upload = round(speed_test.upload() / 1000000, 1)
        print(upload, "Mbps")

        print('1) Ping: ', end='')
        print(speed_test.results.ping)
        data = {"downloads": downloads, "uploads": upload, "ping": int(speed_test.results.ping), "serverLocation": res["name"]}
        with open('/var/www/localhost/htdocs/data.json', 'w') as outfile:
            json.dump(data, outfile)
        print("done")
    except Exception as e:
        print(e)


print("Start testing")

while True:
    st()
    time.sleep(interval * 60)

