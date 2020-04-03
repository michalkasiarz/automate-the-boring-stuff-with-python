import imapclient, pyzmail

# imap client

conn = imapclient.IMAPClient("imap.gmail.com", ssl=True)

# logging in
conn.login("mailboxtest522@gmail.com", "xxxxxx")

# selecting folder in readonly mode
conn.select_folder("INBOX", readonly=True)

# searching emails
UIDs = conn.search(['SINCE', '02-Apr-2020'])
print("Messages UIDs: + " + str(UIDs))

# fetching email
raw_message = conn.fetch([8], ['BODY[]', 'FLAGS'])
