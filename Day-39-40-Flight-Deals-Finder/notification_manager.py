from dotenv import load_dotenv
import os
from twilio.rest import Client
import smtplib

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.smtp_address = os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"]
        self.email = os.environ["MY_EMAIL"]
        self.email_password = os.environ["MY_EMAIL_PASSWORD"]
        self.client = Client(os.environ.get('TWILIO_SID'), os.environ.get('TWILIO_AUTH_TOKEN'))
        self.connection = smtplib.SMTP(os.environ["EMAIL_PROVIDER_SMTP_ADDRESS"], 587)
        
    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=os.environ.get('TWILIO_VIRTUAL_NUMBER'),
            to=os.environ.get('TWILIO_VERIFIED_NUMBER'),
            body=message_body
        )
        print(message.sid)
    
    def send_emails(self, email_list, email_body):
        with self.connection:
            self.connection.starttls()
            self.connection.login(user=self.email, password=self.email_password)
            for email in email_list:
                self.connection.sendmail(
                    from_addr=self.email, 
                    to_addrs=email,
                    msg=f"Subject: New Low Price Flight!\n\n{email_body}".encode('utf-8')
            )


