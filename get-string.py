import yagmail
from dotenv import load_dotenv
import json
import requests
import os


def get_data(key):
    # get string from pastebin
    url = "https://pastebin.com/raw/" + key
    response = requests.get(url)
    # convert string to json object

    return json.loads(response.text)


def send_mail(recipient, subject, content):

    receiver = recipient
    body = content

    yag = yagmail.SMTP(os.environ["mail"], os.environ["pass"])
    yag.send(
        to=receiver,
        subject=subject,
        contents=body,
    )


# get key from config.json one line


fromWeb = get_data(json.loads(open("config.json").read())["pastebin_key"])


reciever = fromWeb['to']
subject = fromWeb['subject']
content = fromWeb['content']

# load .env file
load_dotenv()

# send mail to reciever with subject and content
print("Sending mail to " + reciever + " with subject " +
      subject + " and content " + content)
send_mail(reciever, subject, content)
