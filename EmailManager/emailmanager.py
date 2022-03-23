from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from re import T
import smtplib, ssl
import EMAIL_KEYS


# ----------------------------------------------------------------------------
"""
    Use the requests library to make an API call to Open Weather. If the 
        request is successful, return the requestd data as a JSON data set.
        If the request fails, return None data type. The None response is to
        be handled by the caller of the function
"""
def send_text_email(email_text, subject, send_to):
    send_from = EMAIL_KEYS.HERMES_EMAIL_USER

    msg = MIMEMultipart('alternative')

    if subject is not None:
        msg['Subject'] = subject
    else:
        msg['Subject'] = 'No Subject Given!'
    msg['From'] = send_from
    msg['To'] = ", ".join(send_to)

    msg.attach(MIMEText(email_text, 'plain'))

    try:
        # Start SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        # Enable Extra security
        server.starttls()
        server.login(EMAIL_KEYS.HERMES_EMAIL_USER, EMAIL_KEYS.HERMES_EMAIL_PASSWORD)
        server.send_message(msg, send_from, send_to)
        print('Success!')
    except Exception as ex:
        print('Oops...', ex)


if __name__ == '__main__':    
    txt = '''
    Hello!
    How are you?

    -- Hermes
    '''

    subject = 'Testing My Fancy New Email Service!'

    send_text_email(txt, subject, EMAIL_KEYS.RECIPIENTS)