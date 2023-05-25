from email.message import EmailMessage
import ssl
import os
import smtplib
email_sender = "shahil.official.college@gmail.com"
pwd_sender = os.environ.get("Email_Password")
receiver ="kshahil1999@gmail.com"

subject = "hellow"
body ="apple ball"
em = EmailMessage()
em['From'] = email_sender

em['To'] = receiver
em['Subject'] = subject
em.set_content(body)
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender, pwd_sender)
    smtp.sendmail(email_sender,receiver, em.as_string())
