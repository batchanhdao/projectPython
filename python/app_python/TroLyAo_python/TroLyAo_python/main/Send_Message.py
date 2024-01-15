import Mouth
import Ears
import Stop
import Understand as hieu
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl

smtp_server = "smtp.gmail.com"
sender_email = "lea81807@gmail.com"  # Enter your address
password = 'hqenlurtqbhpedka'

def send_gmail(receiver_email, subject, body):
    try:
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message["Bcc"] = receiver_email

        message.attach(MIMEText(body, "plain"))
        content = message.as_string()
        text = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, 465, context=text) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, content)
        Mouth.speak('Email của bạn vùa được gửi. Bạn check lại email nhé.')
    except Exception as e:
        Mouth.speak(f"lỗi gửi tin cho {receiver_email}")
        print(e)
    finally:
        server.close()