from __future__ import print_function
import io
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from apiclient.http import MediaFileUpload, MediaIoBaseDownload
import time
import concurrent.futures
SCOPES = ['https://www.googleapis.com/auth/drive']
secretCred = 'credentials.json'

class downloader():

    service = None

    def __init__(self, creds):
        self.creds = creds
    
    def createService(self):
        self.service = build('drive', 'v3', credentials=self.creds)

    def download(self, tag):
        
        fileid = (tag.split('::')[0])
        name = (tag.split('::')[1]).split(',')[0]

        request = (self.service).files().get_media(fileId=fileid)
        fh = io.BytesIO()
        print(f"HIT: {name}")
        downloading = MediaIoBaseDownload(fh, request)
        done = False
        while done is False:
            status, done = downloading.next_chunk()
            print(f"GET {name}: {(int(status.progress() * 100))}%.")
        with io.open(name,'wb') as f:
            

    def getList(self):
        results = self.service.files().list(
        pageSize=3, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        itemList = []
        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print(u'{0} ({1})'.format(item['name'], item['id']))
                itemList.append(item['id'] + "::" + item['name' ])

            with open("itemList.txt", 'w') as f:
                for item in itemList:
                    f.write(item+",\n")


    def downloadFromList(self):
        lines = None
        with open("itemList.txt", 'r') as itemList:
            lines = itemList.readlines()
        
        i = 0
        tags = []
        # ids = []

        for line in lines:
            i+=1
            tags.append(line)

        tags.pop()

        # for tag in tags:
        #     print(tag)

        t1 = time.perf_counter()
        
        with concurrent.futures.ThreadPoolExecutor() as exe:
            exe.map(self.download, tags)
        
        
        t2 = time.perf_counter()
        print(f"{i} files downloaded in {t2-t1}s!")
