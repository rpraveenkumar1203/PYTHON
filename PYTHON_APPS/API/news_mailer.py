import smtplib as smtp
import ssl



def send_email(message):
    username = 'rpraveenkumar1203@gmail.com'
    receiver = 'rpraveenkumar1203@gmail.com'
    password = "qflhtaqvayqwwkqs"

    host = 'smtp.gmail.com'
    port = '465'
    context = ssl.create_default_context()
    with  smtp.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.sendmail(username,receiver,message)

