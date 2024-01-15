import smtplib, ssl
smtp_server = "smtp.gmail.com"
sender_email = "lea81807@gmail.com"  # Enter your address
password = 'hqenlurtqbhpedka'

def send_mail():
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    receiver_email = 'leanh17101601@gmail.com'
    # Tạo một tin nhắn nhiều phần và đặt tiêu đề
    subject='send mail'
    body = 'good morning'
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  

    message.attach(MIMEText(body, "plain"))

    filename = "C:\\Users\\lea81\\Downloads\\download.jpg"  # In same directory as script
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    message.attach(part)
    text = message.as_string()

    try:
        text = message.as_string()
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        print('successful {}'.format(receiver_email))
    except Exception as e:
        print(e)
    finally:
        server.close()

#-----------------------------------------
def send_mail_addFile():
    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    with open('ds_receiver.txt','r') as data:
        ds_receiver_mail = data.readlines()
        for text_line in ds_receiver_mail:
            receiver_email, files = text_line.strip('\n').split(';',1)
            receiver_email=receiver_email.strip()
            
            # Tạo một tin nhắn nhiều phần và đặt tiêu đề
            subject='send mail'
            body = f'good morning {receiver_email}'
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message["Bcc"] = receiver_email  # Recommended for mass emails
             # Add body to email
            message.attach(MIMEText(body, "plain"))

            try:
                files = [str(x).strip() for x in files.split('&')]
                # read file
                for file in files:
                    filename = file  # In same directory as script
                    # Open PDF file in binary mode
                    with open(filename, "rb") as attachment:
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(attachment.read())

                    # Encode file in ASCII characters to send by email    
                    encoders.encode_base64(part)

                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename= {filename}",
                    )

                    # Add attachment to message 
                    # Thêm tệp đính kèm vào tin nhắ  
                    message.attach(part)
                    print('successful {}'.format(filename))
            except Exception as e:
                print(e)
                # continue

            finally:
                try:
                    # convert message to string
                    # chuyển đổi tin nhắn thành chuỗi
                    text = message.as_string()
                    # Log in to server using secure context and send email
                    context = ssl.create_default_context()
                    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
                        server.login(sender_email, password)
                        server.sendmail(sender_email, receiver_email, text)
                    print('successful {}'.format(receiver_email))
                except Exception as e:
                    print(e)
                finally:
                    server.close()

# send_mail()
send_mail_addFile()
