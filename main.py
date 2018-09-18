from twilio.rest import Client

def sendSMS (source, destination, body):
    # Check if source number is valid
    destinationNumber = input("What number would you like to send to? ")
    messageContents = input("What would you like to say? ") or "I couldn't be bothered to type a message"
    message = client.messages.create(
        to=destinationNumber,
        from_=sourceNumber,
        body=messageContents)
    print(message)


running = True

account_sid = input("What is your account SID? ")
auth_token = input("What is your auth token? ")

client = Client(account_sid, auth_token)

sourceNumber = input("What number would you like to send from? ")


while running:
    command = input("Would you like to send a message? ") or "yes"
    if command.lower() == "yes":
        destinationNumber = input("What number would you like to send to? ")
        messageContents = input("What would you like to say? ") or "I couldn't be bothered to type a message"
        sendSMS(sourceNumber, destinationNumber, messageContents)
