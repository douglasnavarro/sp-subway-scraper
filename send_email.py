import smtplib

fromaddr = 'sp.subway.scraper@gmail.com'
username = fromaddr
password = 'Asimovs04!'
toaddr  = 'douglasnavarro94@gmail.com'

msg = "\r\n".join([
  "From: sp.subway.scraper@gmail.com",
  "To: douglasnavarro94@gmail.com",
  "Subject: sp-subway-scraper-debug",
  "",
  "Why, oh why"
  ])

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, msg)
server.quit()