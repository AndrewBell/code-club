import os
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC6fa011d56978b8885337d4b33878daf5'
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages.create(
     body="Python is okay, I guess",
     from_='+18482333739',
     to='+16362533739'
 )

print("Message sent with ID %s" %(message.sid,))
