import smtplib
import ssl
import os

def mail(receiver, message):
    host = "smtp.gmail.com"
    port = 465
    username = "MeghnadEmailAssistant"
    #Previously password = "xyvhgosniqcpwojp"
    password = os.getenv("MEGHNADPASS")
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
