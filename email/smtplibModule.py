import smtplib, logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

# logging.disable(logging.CRITICAL)
# Log levels:
# logging.DEBUG (the lowest)
# logging.INFO
# logging.WARNING
# logging.ERROR
# logging.CRITICAL (the highest)

# Simple Mail Transfer Library

logging.debug("Start of program")

# mail server config
conn = smtplib.SMTP("smtp.gmail.com", 587)
logging.debug("Mail server configuration: " + str(conn))

# connecting to the server
conn.ehlo()
logging.debug("Connecting to the server: " + str(conn.ehlo()))
conn.starttls()


# logging into email
conn.login("mailboxtest522@gmail.com", "xxxxxx")
logging.debug("Logging into email: " + str(conn.login("mailboxtest522@gmail.com", "xxxxxx")))

# sending an email
try:
    conn.sendmail("mailboxtest522@gmail.com", "mailboxtest522@gmail.com",
                  "Subject: Test email\n\nDear, Man,\n\nhope you are well.\n\nYours,\nMe.")
    print("Mail sent.")
    conn.quit()
except:
    print("Error occured.")
