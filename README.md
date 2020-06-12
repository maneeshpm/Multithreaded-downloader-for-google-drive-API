# Multithreaded-downloader-for-google-drive-API
This is a python application to download multiple files from your google drive with threading. The application use Google-Drive-API to perform authentication and get the files. All these functions are integrated using a simple and pretty Python Click command line interface, so you can download all those files without having to go through the hassle of ctr-selecting all the individual files on the browser. 

On an average, the time taken for threaded downloading was almost </b>3X Less</b> than the regular downloading which enough for this app to make a point :grin:. You may notice(in the trial runs below) that in threaded download, the downloading of all files begin simultaneously whereas in the normal download its in a queued manner.


## Using the application
<i>Generate a credential.json file from your google drive api portal. Make sure this file is in the same directory as the application</i>

Use `python3 main.py --help` to get help!
- Generate a list of files available in your drive
```
$ python3 main.py gl              
Files:
Screenshot from 2020-05-13 18-56-13.png (**********6xP2Y50x4BejmsGan_coEC)
Screenshot from 2020-04-28 13-36-41.png (**********wM7ecteK47JQHi6g-nPCI_x)
Screenshot from 2020-04-25 12-20-31.png (**********aH163x5BKNKkSFzG5TwZgdO)
Screenshot from 2020-04-13 12-50-45.png (**********GjhY3rA0TBBquQWrlLZA9kQ)
Screenshot from 2020-04-13 12-50-44.png (**********yB6eZaj1KX6r9pcC5Vp2f-e)
----------------------------------------------------
Action Completed! 5 rows written to itemList.csv
```
- Download the files in `itemList.csv` with threading
```
$ python3 main.py td                           
HIT: Screenshot from 2020-05-13 18-56-13.png
HIT: Screenshot from 2020-04-28 13-36-41.png
HIT: Screenshot from 2020-04-25 12-20-31.png
HIT: Screenshot from 2020-04-13 12-50-45.png
HIT: Screenshot from 2020-04-13 12-50-44.png
GET: Screenshot from 2020-05-13 18-56-13.png
GET: Screenshot from 2020-04-28 13-36-41.png
GET: Screenshot from 2020-04-13 12-50-45.png
GET: Screenshot from 2020-04-13 12-50-44.png
GET: Screenshot from 2020-04-25 12-20-31.png
----------------------------------------------------------
Action Completed! 5 Files downloaded, 0m 4s Elapsed 
```
- Download the files in `itemList.csv` without threading(just to compare the speed and prove the point :sweat_smile:)
```
$ python3 main.py rd                            
HIT: Screenshot from 2020-05-13 18-56-13.png
GET: Screenshot from 2020-05-13 18-56-13.png
HIT: Screenshot from 2020-04-28 13-36-41.png
GET: Screenshot from 2020-04-28 13-36-41.png
HIT: Screenshot from 2020-04-25 12-20-31.png
GET: Screenshot from 2020-04-25 12-20-31.png
HIT: Screenshot from 2020-04-13 12-50-45.png
GET: Screenshot from 2020-04-13 12-50-45.png
HIT: Screenshot from 2020-04-13 12-50-44.png
GET: Screenshot from 2020-04-13 12-50-44.png
----------------------------------------------------------
Action Completed! 5 Files downloaded, 0m 15s Elapsed 
```


