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

# using pyzmail36 (not pyzmail!) module
message = pyzmail.PyzMessage.factory(raw_message[8][b'BODY[]'])

# printing subject of the email
print("E-mail subject: " + message.get_subject())    # How's Friday?

# printing the sender
print("Sender: " + str(message.get_addresses("from")))

# printing the receiver
print("Receiver: " + str(message.get_addresses("to")))

# printing the message
print("".center(50, "-"))
print(message.text_part.get_payload().decode("UTF-8"))
print("".center(50, "-"))
