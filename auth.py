import pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path

class Auth:

    def __init__(self, clientSecretKeyFile, SCOPES):
        self.creds = None
        self.clientSecretKeyFile = clientSecretKeyFile
        self.SCOPES = SCOPES

    def getCredentials(self):    
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.clientSecretKeyFile, self.SCOPES)
                creds = flow.run_local_server(port=0)

                with open('token.pickle','wb') as token:
                    pickle.dump(creds, token)
        return creds
