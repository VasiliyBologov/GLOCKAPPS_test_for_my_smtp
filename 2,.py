from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import random
import os
import textile


def send_test_mails(key, to):
    emails = to
    key = key

    you = emails.split("; ")

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

    # print(you)

    """name_sender = 'SethDenvers'
    me = 'seth.d@' + domain
    to_send = 'vasilii.b@xor.ai'
    to = 'Vaso'"""
    # random name

    f1name = open(os.getcwd() + '/first_names.all.txt')

    firstnamebase = f1name.readlines()
    f1name.close()

    f2name = open(os.getcwd() + '/last_names.all.txt')

    lastnamebase = f2name.readlines()
    f2name.close()
    # no '\n'
    firstnamebase = [line.rstrip() for line in firstnamebase]
    lastnamebase = [line.rstrip() for line in lastnamebase]
    # title
    firstnamebase = [line.title() for line in firstnamebase]
    lastnamebase = [line.title() for line in lastnamebase]



    rand_1name = random.randint(0, len(firstnamebase) - 1)
    rand_2name = random.randint(0, len(lastnamebase) - 1)

    me = firstnamebase[rand_1name].lower() + "." + lastnamebase[rand_2name].lower()[0] + "@" + domain

    print(me)

    name_sender = firstnamebase[rand_1name] + lastnamebase[rand_2name]


    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative',)
    msg['Subject'] = "Thank you for your application!"
    msg['FROM'] = name_sender + "<" + me + ">"
    # msg['TO'] = to + "<" + to_send + ">"
    msg['To'] = ','.join(you)
    msg['Return-Path'] = "<bounse@" + domain + ">"
    msg['Precedence'] = 'bulk'
    msg['X-Mailer'] = "XOR from <" + domain + ">"
    msg['X-Auto-Response-Suppress'] = 'OOF, AutoReply'
    msg['X-Report-Abuse'] = 'Please report abuse for this campaign here: https://xorte.ch.com/abuse/'
    msg['List-Unsubscribe'] = "<mailto:unsu@" + domain + "?subject=unsubscribe>"
    msg['List-Unsubscribe-Post'] = 'List-Unsubscribe=One-Click'
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

    """ + firstnamebase[rand_1name] + """ """ + lastnamebase[rand_2name] + """ 

    Head of Sales and Business Development at XOR"""

    html = """
            <html>
              <head></head>
              <body>
                <p>""" + textile.textile(text_mail, html_type='xhtml') + """
                </p>
              </body>
            </html>
            """


    part2 = MIMEText(text_mail, 'plain')
    #part2.replace_header('content-transfer-encoding', 'quoted-printable')
    part1 = MIMEText(html, 'html')
    #part1.replace_header('content-transfer-encoding', 'quoted-printable')

    msg.attach(part1)
    msg.attach(part2)



    s = smtplib.SMTP(server, port)
    # s.ehlo()

    s.sendmail(me, you, msg.as_string())
    print("OK")





if __name__ == '__main__':
    print("hello")
    test_number = 1
    while True:
        print('Test # ' + str(test_number))
        print('Vvedi key')
        k = input()
        print("Vvedo pochti")
        t = input()
        send_test_mails(k, t)
        print("next test? y -yes n - no")
        answer = input()
        if answer == 'n':
            print("bye")
            break
        elif answer == 'y':
            print('next test run')
            test_number =+ 1
        else:
            print("Otvet ne yasen")
            print("bye")
            break