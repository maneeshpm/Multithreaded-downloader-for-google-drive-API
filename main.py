from auth import Auth
from DownloadManager import DownloadManager
import click

SCOPES = ['https://www.googleapis.com/auth/drive']
clientSecretKey = 'credentials.json'

newAuth = Auth(clientSecretKey, SCOPES)
newCreds = newAuth.getCredentials()
newDownloadManager = DownloadManager(newCreds)

@click.group()
def main():
    """Script to download files from google drive using Google Drive API"""
    pass

@main.command()
def gl():
    """Generate a list of all items in your drive as a CSV file"""
    newDownloadManager.getList()

@main.command()
def td():
    """Download items specified in itemList.csv with threading"""
    newDownloadManager.downloadFromListThread('itemList.csv')

@main.command()
def rd():
    """Download items specified in itemList.csv without threading"""
    newDownloadManager.downloadFromListRegular('itemList.csv')

if __name__ == '__main__':
    main()