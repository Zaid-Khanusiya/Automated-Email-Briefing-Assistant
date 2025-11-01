from simplegmail import Gmail
from google import genai
import os
from prompts import *
import requests
import json

GOOGLE_GENAI_API_KEY = os.getenv("GOOGLE_GENAI_API_KEY")

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

genai_client = genai.Client(api_key=GOOGLE_GENAI_API_KEY)
genai_model = "gemini-2.5-flash"

gmail_client = Gmail()

def read_new_mails():
    messages = gmail_client.get_unread_inbox()
    # messages = gmail_client.get_messages()

    messages_list = []

    for message in messages:
        message.mark_as_read()
        messages_list.append({
            'sender': message.sender,
            'subject_line': message.subject,
            'body': message.plain
        })

    return messages_list

def summarise_email_list(emails_list):
    model_prompt = get_summarise_email_list_prompt(email_list=emails_list)
    response = genai_client.models.generate_content(
        model = genai_model,
        contents = model_prompt
    )
    return response.text

def forward_to_slack_channel(content):
    payload = {
        "text": content,
        "username": "Email-Summary-Bot"
    }

    response = requests.post(
        SLACK_WEBHOOK_URL, data=json.dumps(payload),
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code == 200:
        return True
    else:
        return False