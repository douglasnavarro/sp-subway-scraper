import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

COMMASPACE = ', '

def send_email(attachment):

    sender = os.environ.get('SENDER', None) 
    gmail_password  = os.environ.get('GMAIL_PASSWORD', None)
    recipients   = ['douglasnavarro94@gmail.com']

    outer = MIMEMultipart()
    outer['Subject'] = 'Debug scraper'
    outer['To'] = COMMASPACE.join(recipients)
    outer['From'] = sender
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'

    # msg = "\r\n".join([
    # "From: sp.subway.scraper@gmail.com",
    # "To: douglasnavarro94@gmail.com",
    # "Subject: sp-subway-scraper-debug",
    # "",
    # body
    # ])

    msg = MIMEBase('application', "octet-stream")
    msg.set_payload(attachment)
    encoders.encode_base64(msg)
    msg.add_header('Content-Disposition', 'attachment', filename='viaquatro.html')
    outer.attach(msg)

    composed = outer.as_string()

    with smtplib.SMTP('smtp.gmail.com', 587) as s:
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login(sender, gmail_password)
        s.sendmail(sender, recipients, composed)
        s.close()
    print("Email sent!")