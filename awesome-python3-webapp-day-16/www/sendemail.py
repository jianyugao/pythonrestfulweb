def send_email(user, pwd, recipient, subject, body):
    import smtplib

    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
#         server_ssl = smtplib.SMTP_SSL("smtp.googlemail.com", 465)
#         server_ssl.ehlo() # optional, called by login()
#         server_ssl.login(gmail_user, gmail_pwd)  
# # ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
#         server_ssl.sendmail(FROM, TO, message)
# #server_ssl.quit()
#         server_ssl.close()
        # import pdb
        # pdb.set_trace()
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ('successfully sent the mail')
    except:
        print ("failed to send mail")
if __name__ == '__main__':
    sendmail = send_email(user='animeoneblog@gmail.com', pwd='123chenqwer',recipient='jianyugpku@gmail.com',
        subject='testemail', body='chenggongle')