from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib
import EMAIL_KEYS


# ----------------------------------------------------------------------------
"""
    Use the stmplib package to send a basic text email

    Inputs:
        email_text -> Text body of email to send
        subject -> Text subject line for email
        send_to -> List containing all of the recipients of the email
    
    Output:
        Print Success/Failure to terminal
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

    send_text_email(txt, subject, [EMAIL_KEYS.RECIPIENTS[0]])