from twilio.rest import Client

running = True

account_sid = input("What is your account SID? ")
auth_token = input("What is your auth token? ")

client = Client(account_sid, auth_token)

sendNumber = input("What number would you like to send from? ")


while running:
    command = input("Would you like to send a message? ") or "yes"
    if command.lower() == "yes":
        destinationNumber = input("What number would you like to send to? ")
        messageContents = input("What would you like to say? ") or "I couldn't be bothered to type a message"
        message = client.messages.create(
        to=destinationNumber,
        from_=sendNumber,
        body=messageContents)
        print (message)
