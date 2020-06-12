from googleapiclient.discovery import build
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
import io
import threading
import csv
import time
class DownloadManager:
    def __init__(self, creds):
        self.creds = creds
    
    def downloadFile(self, fid, fname):
        service = build('drive','v3', credentials=self.creds)
        request = service.files().get_media(fileId=fid)
        fh = io.FileIO('{}.png'.format(fname),'wb')
        downloader = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print("GET: {}".format(fname))   


    def getList(self):
        service = build('drive','v3', credentials=self.creds)
        results = service.files().list(
        fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        itemList = []
        
        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))
                itemList.append({'fname':item['name'], 'fid':item['id']})
            i=0
            with open("itemList.csv", 'w') as f:
                
                fieldnames=['fname','fid']
                fwriter = csv.DictWriter(f,fieldnames=fieldnames)
                for item in itemList:
                    i+=1
                    fwriter.writerow(item)
            print("----------------------------------------------------------")
            print("Action Completed! {} rows written to itemList.csv".format(i))

    def downloadFromListThread(self, filePath):
        itemList = []
        with open(filePath,'r') as csvlist:
            csv_reader = csv.DictReader(csvlist, fieldnames=['fname','fid'])
            for row in csv_reader:
                line = {}
                line['fid']=row['fid']
                line['fname']=row['fname']
                itemList.append(line)

        threads = []
        for item in itemList:
            thread = threading.Thread(target=self.downloadFile, args=(item['fid'],item['fname'],)) 
            threads.append(thread)
        
        t1 = time.perf_counter()
        i=0
        for thread in threads:
            thread.start()
            print("HIT: {}".format(itemList[i]['fname']))
            i+=1
        
        i=0
        for thread in threads:
            thread.join()
            i+=1
        
        t2 = time.perf_counter()
        print("----------------------------------------------------------")
        print("Action Completed! {} Files downloaded, {}m {}s Elapsed ".format(i, int((t2-t1)/60), int(t2-t1)%60))

    def downloadFromListRegular(self, filePath):
        with open(filePath,'r') as csvlist:
            csv_reader = csv.DictReader(csvlist, fieldnames=['fname','fid'])
            t1 = time.perf_counter()
            i = 0
            for row in csv_reader:
                print("HIT: {}".format(row['fname']))
                self.downloadFile(row['fid'],row['fname'])
                i+=1
            t2 = time.perf_counter()
            print("----------------------------------------------------------")
            print("Action Completed! {} Files downloaded, {}m {}s Elapsed ".format(i, int((t2-t1)/60), int(t2-t1)%60))
                



