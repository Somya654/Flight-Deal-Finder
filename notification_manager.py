from twilio.rest import Client

TWILIO_SID = "ACa974dd2ee5c8e8fbdaeb227a005b0abf"
TWILIO_AUTH_TOKEN = "f6d7f3388f48808bbfa5b22c984c25b1"
TWILIO_VIRTUAL_NUMBER = '+12294412632'
TWILIO_VERIFIED_NUMBER = '+918962421747'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)