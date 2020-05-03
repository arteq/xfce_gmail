# Why create new plugin?
Because that's insane that in 2020 a mature project like Xfce can't handle such a simple task as email monitor for the most popular email service like Gmail without some hacking, allowing unsecure access and so on...

# What this plugin does?
It simply checks if you have any unread emails in your Gmail INBOX. Display one icon if there are new emails, another otherwise. It's dead simple, has no configuration, checks only for INBOX, for only one account. Uses standard Xfce genmon for icon display in menubar. Most important thing: secure OAuth is used which means no username/password and no need to allow less secure apps to access your google account.

# Installation
```sh
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
cd ~/.config/xfce4
git clone !!! 
```

1. goto: https://developers.google.com/gmail/api/quickstart/python 
2. click **Enable the Gmail API** 
3. Choose 'Desktop app'
4. Download client configuration
5. Move downloaded **credentials.json** to ~/.config/xfce4/xfce_gmail/
6. Run the script for the first time:
```sh
cd ~/.config/xfce/xfce_gmail
python gmail.py
```
7. A browser should open with OAuth request. Once accepted a token.pickle will be saved for futher requests.
8. Add generic monitor to your menubar: right click on menu, Panel > Add applet > GenMon
9. Configure genmon applet: right click on new applet > properties > command: 


# Credits
The script is almost exact copy of an example app from google docs: https://developers.google.com/gmail/api/quickstart/python
Mail icons are copied from Xfce (just for convenience)

