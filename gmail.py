from __future__ import print_function
import pickle
import os.path
import sys
from pprint import pprint
from inspect import getmembers
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

ICON_NEWMAIL = "/icons/xfce-newmail.png"
ICON_NOMAIL = "/icons/xfce-nomail.png"


def get_script_path():
    return os.path.dirname(os.path.realpath(sys.argv[0]))

def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    path = get_script_path();

    if os.path.exists(path + '/token.pickle'):
        with open(path + '/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                path + '/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(path + '/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # get unread
    unread = service.users().messages().list(userId='me', labelIds=['UNREAD'], maxResults=10).execute();

    messages = []
    if 'messages' in unread:
        messages.extend(unread['messages'])

    if (len(messages) > 0):
        print('<img>%s</img>' % path + ICON_NEWMAIL)
        print('<tool>%d unread emails</tool>' % len(messages))
    else:
        print('<img>%s</img>' % path + ICON_NOMAIL)
        print('<tool>No unread emails</tool>')

if __name__ == '__main__':
    main()
