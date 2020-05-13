# Why create new plugin?
Because that's insane that in 2020 a mature project like Xfce can't handle such a simple task as email monitor for the most popular email service like Gmail without some hacking or allowing unsecure access to Gmail account.

# What this plugin does?
It simply checks if you have any unread emails in your Gmail INBOX. Display one icon if there are any new emails, another icon otherwise. It's dead simple, has no configuration, checks only for INBOX (that's IMAP folder), for only one email account. Uses standard Xfce genmon for icon display in menubar. Most important thing: secure OAuth is used which means no username/password and no need to allow less secure apps to access your google account.

# Installation

1. Install google OAuth stuff and clone this repository:

   ```sh
   pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
   cd ~/.config/xfce4
   git clone https://github.com/arteq/xfce_gmail
   ```

2. Goto: https://developers.google.com/gmail/api/quickstart/python 

3. Click **Enable the Gmail API** 

4. Choose **Desktop app**

5. Download client configuration

6. Move downloaded **credentials.json** to `~/.config/xfce4/xfce_gmail/`

7. Run the script for the first time:

   ```sh
   cd ~/.config/xfce4/xfce_gmail
   python gmail.py
   ```

8. A browser should open with OAuth request. Once accepted a **token.pickle** file will be saved for any futher requests. 

9. Add generic monitor applet to your menubar: right click on menubar, **Panel > Add New Items...**. Choose **Generic Monitor** from the list and close the popup.

   ![screen1](../media/scr1.jpg?raw=true)

10. Configure genmon applet: right click on new applet: **Properties > Command** and put: `python ~/.config/xfce4/xfce_gmail/gmail.py` 

   You probably want disable the label display and adjust the check interval.

   ![screen3](../media/scr3.jpg?raw=true)

11. You're done!


# Credits
The script is almost exact copy of an example app from google docs: https://developers.google.com/gmail/api/quickstart/python
Mail icons are copied from Xfce (just for convenience, you can always update icons path in the script for something you like more).
