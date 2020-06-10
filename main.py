from auth import auth
from downloader import downloader

SCOPES = ['https://www.googleapis.com/auth/drive']
secretCred = 'credentials.json'

newAuth = auth(SCOPES, secretCred)
cred = newAuth.getAuth()

newDownloader = downloader(cred)
newDownloader.createService()

newDownloader.getList()
newDownloader.downloadFromList()
# newDownloader.download('1xf9SigkYdGjhY3rA0TBBquQWrlLZA9kQ::Screenshot from 2020-04-13 12-50-45.png,\n')