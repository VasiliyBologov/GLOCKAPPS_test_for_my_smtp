from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import datetime
import os


emails = "ipm13ho@glockapps.com; allanb@glockapps.awsapps.com; markb@glockapps.awsapps.com; bcc@spamcombat.com; chazb@userflowhq.com; stevebarrydr@fastmail.com; verify79@buyemailsoftware.com; verifycom79@gmx.com; gd@desktopemail.com; jpatton@fastdirectorysubmitter.com; b2bdeliver79@mail.com; glockapps@mc.glockapps.com; nsallan@expertarticles.com; exosf@glockeasymail.com; sa79@justlan.com; verifynewssl@zoho.com; lamb@glockdb.com"



key = " id:2020-05-20-21:54:58:850t"

you = emails.split("; ")

#print(you)

# smtp data & connect
psmtp = os.getcwd() + "/settings/smtp.my"
fsmtp = open(psmtp, 'r')
smtpset = fsmtp.readlines()
smtpset = [line.rstrip() for line in smtpset]
# print(smtpset)
fsmtp.close()
server = smtpset[0]
port = smtpset[1]
domain = smtpset[2]
s = smtplib.SMTP(server, port)
#s.ehlo()



name_sender = 'SethDenvers'
me = 'seth.d@' + domain
to_send = 'vasilii.b@xor.ai'
to = 'Vaso'

you = emails.split("; ")



# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Thank you for your application!"
msg['FROM'] = name_sender + "<" + me + ">"
#msg['TO'] = to + "<" + to_send + ">"
msg['To'] = ','.join(you)
msg['List-Unsubscribe'] = "unsu@" + domain
msg['Precedence'] = 'bulk'
html = """<!DOCTYPE html> <html><body>hank you for applying for our new vacancy as Area Manager - San Francisco, CA and showing a keen interest in our company, XOR Application.


 

I am your virtual assistant and I will be glad to lead you during the hiring process.

Here at XOR Application, we are always looking to collaborate with talented people [who’d like to work with one of our clients, like X, Y, Z companies.]

 

We are currently looking for a [Successful Candidate Description] to join our team.

I’d love to tell you a little more about this position and learn a few things about you, as well.

Pl     """ + key + """

 

Thank you, again, for your interest in our company. We do appreciate the time that you invested in this application.

 

I hope you have a great day!

XOR Team.


With best regards,

Seth Denvers 

Head of Sales and Business Development at XOR</body></html>"""
text_mail = """hank you for applying for our new vacancy as Area Manager - San Francisco, CA and showing a keen interest in our company, XOR Application.

 

I am your virtual assistant and I will be glad to lead you during the hiring process.

Here at XOR Application, we are always looking to collaborate with talented people [who’d like to work with one of our clients, like X, Y, Z companies.]

 

We are currently looking for a [Successful Candidate Description] to join our team.

I’d love to tell you a little more about this position and learn a few things about you, as well.

Pl  """ + key + """
 

Thank you, again, for your interest in our company. We do appreciate the time that you invested in this application.

 

I hope you have a great day!

XOR Team.


With best regards,

Seth Denvers 

Head of Sales and Business Development at XOR"""


part2 = MIMEText(text_mail, 'plain')
part1 = MIMEText(html, 'html')

msg.attach(part1)
msg.attach(part2)


s.sendmail(me, you, msg.as_string())
print("OK")
